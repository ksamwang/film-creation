#!/usr/bin/env python3
"""Check skill routing: description triggers, routing-table paths, routed templates and layer entries,
reachability of every reference file from SKILL.md, bare filename references, and README parity."""

import collections
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT, ".claude", "skills", "film-creation")
SKILL = os.path.join(SKILL_DIR, "SKILL.md")
README = os.path.join(ROOT, "README.md")

DESCRIPTION_MAX = 1024
# One or more keywords per area; the description must mention at least one from each group.
TRIGGERS = {
    "故事 / 剧本": ["故事", "剧本"],
    "台词": ["台词", "对白"],
    "叙事技巧": ["伏笔", "反转"],
    "类型": ["悬疑", "类型"],
    "treatment": ["treatment", "梗概"],
    "角色一致": ["角色"],
    "分镜脚本": ["分镜脚本"],
    "连续性 / 节奏": ["连续性", "节奏"],
    "镜头语言": ["镜头语言", "运镜"],
    "多镜头视频提示词": ["多镜头"],
    "生成方式": ["首尾帧", "生成方式"],
    "选模型": ["选模型"],
    "参考图": ["参考图"],
    "声音剪辑": ["配乐", "剪辑"],
    "风格参考": ["风格参考", "风格卡"],
    "短剧": ["竖屏短剧", "短剧"],
    "English": ["Triggers:"],
}
UNROUTED_TEMPLATES_OK = {"director-entry.md"}  # authoring template for director profiles, not a user deliverable
UNREACHABLE_OK = {"templates/director-entry.md"}
LAYER_ENTRIES = ["references/craft/index.md", "references/writing/index.md", "references/storyboard/index.md",
                 "references/video-prompt/index.md", "references/camera/index.md", "references/drama/index.md"]

PATH = re.compile(r"`([A-Za-z0-9_./<>-]+?\.md)`")
LINK = re.compile(r"`([A-Za-z0-9_./<>-]+?\.md)`|\]\(([A-Za-z0-9_./-]+?\.md)\)")

issues = 0


def report(msg: str) -> None:
    global issues
    issues += 1
    print(f"[!] {msg}")


def read(path: str) -> str:
    return open(path, encoding="utf-8").read()


def all_md() -> set:
    files = set()
    for d, _, fs in os.walk(SKILL_DIR):
        for f in fs:
            if f.endswith(".md"):
                files.add(os.path.relpath(os.path.join(d, f), SKILL_DIR).replace(os.sep, "/"))
    return files


def resolve(ref: str, here: str, files: set):
    for base in ("", "references", os.path.dirname(here)):
        p = os.path.normpath(os.path.join(base, ref)).replace(os.sep, "/")
        if p in files:
            return p
    return None


def routing_section(text: str) -> str:
    start = text.index("## 路由表")
    end = text.index("\n## ", start + 1)
    return text[start:end]


def table_paths(section: str) -> list:
    rows = [line for line in section.splitlines() if line.startswith("| ") and not line.startswith("| 用户意图")]
    return [p for row in rows for p in PATH.findall(row)]


def main() -> None:
    files = all_md()
    skill = read(SKILL)

    # 1. Description
    m = re.search(r'^description: "(.*)"$', skill, re.M)
    if not m:
        report("SKILL.md: 没找到带引号的 description")
        desc = ""
    else:
        desc = m.group(1)
        if len(desc) > DESCRIPTION_MAX:
            report(f"SKILL.md: description {len(desc)} 字符，超过 {DESCRIPTION_MAX}")
        for area, words in TRIGGERS.items():
            if not any(w in desc for w in words):
                report(f"SKILL.md: description 缺「{area}」的触发词（{' / '.join(words)}）")
    print(f"[ok] description: {len(desc)} 字符，{len(TRIGGERS)} 组触发词")

    # 2. Routing-table paths
    section = routing_section(skill)
    paths = table_paths(section)
    for p in paths:
        if "<" in p:
            continue
        if "/" not in p:
            report(f"SKILL.md 路由表: `{p}` 只写了文件名，写完整路径")
        elif p not in files:
            report(f"SKILL.md 路由表: 路径不存在 {p}")
    print(f"[ok] 路由表: {len(paths)} 处路径")

    # 3. Every template is routed
    routed = set(paths)
    for name in sorted(os.listdir(os.path.join(SKILL_DIR, "templates"))):
        if name.endswith(".md") and name not in UNROUTED_TEMPLATES_OK and f"templates/{name}" not in routed:
            report(f"templates/{name} 没有出现在路由表里")

    # 4. Layer entry points are named in SKILL.md
    for entry in LAYER_ENTRIES:
        if entry not in skill:
            report(f"SKILL.md 没有提到 {entry}")

    # 5. Reachability from SKILL.md, and bare references that do not resolve
    depth = {"SKILL.md": 0}
    queue = collections.deque(["SKILL.md"])
    while queue:
        here = queue.popleft()
        text = read(os.path.join(SKILL_DIR, here))
        for a, b in LINK.findall(text):
            ref = a or b
            if "<" in ref:
                continue
            target = resolve(ref, here, files)
            if target is None:
                if "/" not in ref:
                    report(f"{here}: `{ref}` 在本目录和 references/ 下都找不到，写完整路径")
                continue
            if target not in depth:
                depth[target] = depth[here] + 1
                queue.append(target)
    unreachable = sorted(files - set(depth) - UNREACHABLE_OK)
    for f in unreachable:
        report(f"{f}: 从 SKILL.md 顺着引用到不了")
    print(f"[ok] 可达: {len(depth)}/{len(files)} 个文件")

    # 6. README mirrors the routing table
    if os.path.exists(README):
        readme = read(README)
        start = readme.index("## 请求路由表")
        end = readme.index("\n## ", start + 1)
        mirror = set(table_paths(readme[start:end]))
        for p in sorted(routed - mirror):
            report(f"README 路由表缺 {p}（SKILL.md 有）")
        for p in sorted(mirror - routed):
            report(f"README 路由表多了 {p}（SKILL.md 没有）")

    print(f"\nChecked routing: {len(paths)} routed paths, {len(depth)} reachable files, {issues} issues.")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
