#!/usr/bin/env python3
"""Check the storyboard lookup layer: files, entry fields, storyboard-script tables, templates, references, routing."""

import glob
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, ".claude", "skills", "film-creation")
REFS = os.path.join(SKILL, "references")
BOARD = os.path.join(REFS, "storyboard")
TEMPLATES = os.path.join(SKILL, "templates")

REQUIRED = ["index.md", "breakdown.md", "shot-functions.md", "three-ways.md", "frames.md",
            "animatic.md", "continuity.md", "pacing.md", "scene-types.md", "example.md", "sources.md"]
FUNCTION_FIELDS = ["**是什么**", "**什么时候要**", "**一场放几个**", "**剧本里**", "**拍法**", "**生成**", "**失败**"]
CONTINUITY_FIELDS = ["**规则**", "**观众察觉**", "**AIGC 常见失败**", "**修法**"]
SCRIPT_FILES = ["breakdown.md", "scene-types.md", "example.md"]
STRUCTURAL_TAGS = {"结尾", "开场"}
GRADES = ("稳", "定帧", "后期")
TEMPLATE_SECTIONS = {
    "storyboard-script.md": ["### 读戏", "### 镜头数", "### 分镜脚本", "### 高风险镜头与备选", "### 审读"],
    "shot-list.md": ["## 批次", "## 逐镜", "## 进度", "## 覆盖检查", "## 一致性"],
}
BANNED = ["演员", "排练", "选角", "剧组", "通告", "灯具", "轨道", "布光", "现场录音", "同期声"]
ROUTES = ["references/storyboard/breakdown.md", "references/storyboard/shot-functions.md",
          "references/storyboard/frames.md", "references/storyboard/continuity.md",
          "references/storyboard/pacing.md", "templates/storyboard-script.md"]
REF = re.compile(r"`((?:references|templates|craft|camera|writing|storyboard|recipes|directors|cinematographers|aigc|drama)/[^`*<>\s]+?\.md)")
BARE = re.compile(r"`([a-z][a-z0-9-]*\.md)`")
ROW = re.compile(r"^\| *(\d+)-(\d+)([A-Z]?) *\|(.*)$", re.M)

issues = 0


def report(msg: str) -> None:
    global issues
    issues += 1
    print(f"[!] {msg}")


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def read(path: str) -> str:
    return open(path, encoding="utf-8").read()


def resolves(ref: str, here: str) -> bool:
    bases = [SKILL, REFS, BOARD, os.path.dirname(here)]
    return any(os.path.exists(os.path.join(b, ref)) for b in bases)


def entries(text: str):
    """Yield (title, body) for each ### entry."""
    parts = re.split(r"^### +(.+)$", text, flags=re.M)
    for i in range(1, len(parts), 2):
        body = re.split(r"^##? ", parts[i + 1], maxsplit=1, flags=re.M)[0]
        yield parts[i].strip(), body


def function_names(path: str) -> set:
    """Chinese names of shot functions, e.g. 「入场 / 出场」 → {入场, 出场}."""
    names = set()
    for title, _ in entries(read(path)):
        zh = re.split(r" [A-Za-z]", title, maxsplit=1)[0]
        for part in zh.split("/"):
            part = part.strip()
            names.add(part)
            names.add(re.sub(r"(镜头|镜)$", "", part))  # 「反应镜」 is used as 「反应」 in scripts
    return names


def check_fields(path: str, fields, skip=lambda title, body: False) -> int:
    n = 0
    for title, body in entries(read(path)):
        if skip(title, body):
            continue
        n += 1
        for field in fields:
            if field not in body:
                report(f"{rel(path)} · {title}: 缺 {field}")
    return n


def check_script(path: str, functions: set) -> int:
    """Validate storyboard-script rows: columns, function, grade, order, and the stated shot count per scene."""
    text = read(path)
    rows = ROW.findall(text)
    groups = []  # consecutive rows sharing a scene number
    for scene, shot, suffix, rest in rows:
        cells = [c.strip() for c in rest.rstrip().rstrip("|").split("|")]
        label = f"{scene}-{shot}{suffix}"
        if len(cells) != 8:
            report(f"{rel(path)} · {label}: 分镜脚本应为 9 列，实际 {len(cells) + 1} 列")
            continue
        func, grade = cells[0], cells[7]
        for part in re.split(r"[/／]", func):
            name = re.sub(r"（.*?）", "", part).strip()
            if name not in functions and name not in STRUCTURAL_TAGS:
                report(f"{rel(path)} · {label}: 功能「{name}」不在 shot-functions.md 里")
        if not any(g in grade for g in GRADES):
            report(f"{rel(path)} · {label}: 生成栏没有写可靠性（稳 / 定帧 / 后期）")
        key = (int(shot), suffix)
        if groups and groups[-1][0] == scene:
            if key <= groups[-1][2]:
                report(f"{rel(path)} · {label}: 镜号没有递增")
            groups[-1][1] += 1
            groups[-1][2] = key
        else:
            groups.append([scene, 1, key])
    stated = [int(n) for n in re.findall(r"\*\*(\d+) 镜\*\*", text)]
    if stated and len(stated) == len(groups):
        for (scene, count, _), want in zip(groups, stated):
            if count != want:
                report(f"{rel(path)} · 场 {scene}: 写的是 {want} 镜，表里有 {count} 镜")
    elif stated:
        report(f"{rel(path)}: 镜头数声明 {len(stated)} 处，分镜脚本 {len(groups)} 场，对不上")
    return len(rows)


def check_common(path: str) -> None:
    text = read(path)
    if os.path.basename(path) != "sources.md" and "storyboard/sources.md" not in text:
        report(f"{rel(path)}: 来源没有指向 storyboard/sources.md")
    for ref in REF.findall(text):
        if not resolves(ref, path):
            report(f"{rel(path)}: 引用不存在 {ref}")
    for name in BARE.findall(text):
        if not os.path.exists(os.path.join(os.path.dirname(path), name)):
            report(f"{rel(path)}: 引用不存在 {name}")
    for word in BANNED:
        if word in text:
            report(f"{rel(path)}: 出现实拍用语「{word}」")


def main() -> None:
    for name in REQUIRED:
        if not os.path.exists(os.path.join(BOARD, name)):
            report(f"缺少 storyboard/{name}")

    index = os.path.join(BOARD, "index.md")
    if os.path.exists(index):
        listed = set(re.findall(r"`([a-z-]+\.md)`", read(index)))
        actual = {os.path.basename(f) for f in glob.glob(os.path.join(BOARD, "*.md"))} - {"index.md"}
        for name in sorted(actual - listed):
            report(f"storyboard/{name} 没有列进 storyboard/index.md")

    functions = set()
    n_functions = 0
    path = os.path.join(BOARD, "shot-functions.md")
    if os.path.exists(path):
        n_functions = check_fields(path, FUNCTION_FIELDS)
        functions = function_names(path)
        print(f"[ok] shot-functions.md: {n_functions} 种功能")

    path = os.path.join(BOARD, "continuity.md")
    if os.path.exists(path):
        n = check_fields(path, CONTINUITY_FIELDS)
        print(f"[ok] continuity.md: {n} 条规则")

    shots = 0
    for name in SCRIPT_FILES:
        path = os.path.join(BOARD, name)
        if os.path.exists(path):
            n = check_script(path, functions)
            shots += n
            print(f"[ok] {name}: {n} 镜")

    sources = os.path.join(BOARD, "sources.md")
    if os.path.exists(sources):
        text = read(sources)
        for name in REQUIRED:
            if name in ("index.md", "sources.md"):
                sec = "## index" if name == "index.md" else None
            else:
                sec = "## " + name[:-3]
            if sec and sec not in text:
                report(f"storyboard/sources.md: 缺小节「{sec}」")

    for name, sections in TEMPLATE_SECTIONS.items():
        path = os.path.join(TEMPLATES, name)
        if not os.path.exists(path):
            report(f"缺少 templates/{name}")
            continue
        text = read(path)
        for sec in sections:
            if sec not in text:
                report(f"templates/{name}: 缺小节「{sec}」")

    for path in sorted(glob.glob(os.path.join(BOARD, "*.md"))):
        check_common(path)

    skill = read(os.path.join(SKILL, "SKILL.md"))
    for route in ROUTES:
        if route not in skill:
            report(f"SKILL.md 没有指向 {route}")

    print(f"\nChecked storyboard layer: {n_functions} functions, {shots} script shots, {issues} issues.")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
