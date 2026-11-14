#!/usr/bin/env python3
"""Check the writing lookup layer: files, entry fields, symptom numbering, genre sections, references, routing."""

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
WRITING = os.path.join(REFS, "writing")
GENRES = os.path.join(WRITING, "genres")

REQUIRED = ["index.md", "dialogue.md", "devices.md", "intent.md", "doctor.md",
            "example.md", "sources.md", "genres/index.md"]
GENRE_FILES = ["suspense.md", "romance.md", "comedy.md", "horror.md", "crime-action.md",
               "scifi-fantasy.md", "family.md", "brand.md"]
GENRE_SECTIONS = ["## 观众在等什么", "## 必备元素", "## 结构", "## 示例", "## 陈词滥调 → 替代",
                  "## 常用技巧", "## 镜头与画面", "## 短剧对应", "## 来源"]
DIALOGUE_FIELDS = ["**改后**", "**作用**"]
DEVICE_FIELDS = ["**是什么**", "**作用**", "**落到产物**", "**失败**"]
SOURCE_SECTIONS = ["## dialogue", "## doctor", "## devices", "## intent", "## genres"]
TEMPLATE = os.path.join(SKILL, "templates", "script.md")
TEMPLATE_SECTIONS = ["## 片头信息", "## Beat 表", "## 技巧与伏笔", "## 正文", "## 台词表", "## 资产", "## 检查"]
BANNED = ["演员", "排练", "选角", "剧组", "通告", "灯具", "轨道", "布光", "现场录音", "同期声"]
ROUTES = ["references/writing/dialogue.md", "references/writing/devices.md",
          "references/writing/intent.md", "references/writing/doctor.md",
          "references/writing/genres/index.md", "templates/script.md"]
REF = re.compile(r"`((?:references|templates|craft|camera|writing|recipes|directors|cinematographers|aigc|drama)/[^`*<>\s]+?\.md)")
BARE = re.compile(r"`([a-z][a-z0-9-]*\.md)`")

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
    bases = [SKILL, REFS, WRITING, os.path.dirname(here)]
    return any(os.path.exists(os.path.join(b, ref)) for b in bases)


def entries(text: str):
    """Yield (title, body) for each ### entry."""
    parts = re.split(r"^### +(.+)$", text, flags=re.M)
    for i in range(1, len(parts), 2):
        body = re.split(r"^##? ", parts[i + 1], maxsplit=1, flags=re.M)[0]
        yield parts[i].strip(), body


def check_dialogue(path: str) -> int:
    n = 0
    for title, body in entries(read(path)):
        if "**改前**" not in body or "**问题**" in body:
            continue  # tables, sheets, rule lists and diagnostic entries
        n += 1
        for field in DIALOGUE_FIELDS:
            if field not in body:
                report(f"{rel(path)} · {title}: 缺 {field}")
    return n


def check_devices(path: str) -> int:
    n = 0
    for title, body in entries(read(path)):
        n += 1
        for field in DEVICE_FIELDS:
            if field not in body:
                report(f"{rel(path)} · {title}: 缺 {field}")
    return n


def check_doctor(path: str) -> int:
    text = read(path)
    quick = re.search(r"## 症状速查(.+?)\n---", text, flags=re.S)
    if not quick:
        report(f"{rel(path)}: 缺「## 症状速查」表")
        return 0
    numbers = [int(x) for x in re.findall(r"^\| *(\d+) *\|", quick.group(1), flags=re.M)]
    if numbers != list(range(1, len(numbers) + 1)):
        report(f"{rel(path)}: 症状编号不连续 {numbers}")
    detail = text[quick.end():]
    for num in numbers:
        if not re.search(rf"^(### {num} |\| *{num} *\|)", detail, flags=re.M):
            report(f"{rel(path)}: 症状 #{num} 只在速查表里，没有展开")
    return len(numbers)


def check_intent(path: str) -> int:
    text = read(path)
    quick = re.search(r"## 速查(.+?)\n---", text, flags=re.S)
    if not quick:
        report(f"{rel(path)}: 缺「## 速查」表")
        return 0
    rows = re.findall(r"^\| *([^|\-][^|]*?) *\|", quick.group(1), flags=re.M)
    effects = [r for r in rows if r != "想要"]
    for effect in effects:
        if not re.search(rf"^## {re.escape(effect)}\s*$", text, flags=re.M):
            report(f"{rel(path)}: 速查里的「{effect}」没有对应小节")
    return len(effects)


def check_genre(path: str) -> None:
    text = read(path)
    for sec in GENRE_SECTIONS:
        if sec not in text:
            report(f"{rel(path)}: 缺小节「{sec}」")
    for tier in ("**60 秒档**", "**3–5 分钟档**"):
        if tier not in text:
            report(f"{rel(path)}: 结构里缺 {tier}")
    if not re.search(r"^\| *# *\|", text, flags=re.M):
        report(f"{rel(path)}: 示例没有 beat 表")
    if "references/drama/01-premise.md" not in text:
        report(f"{rel(path)}: 短剧对应没有指向 drama/01-premise.md")


def check_common(path: str) -> None:
    text = read(path)
    if os.path.basename(path) != "sources.md" and "writing/sources.md" not in text:
        report(f"{rel(path)}: 来源没有指向 writing/sources.md")
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
        if not os.path.exists(os.path.join(WRITING, name)):
            report(f"缺少 writing/{name}")
    for name in GENRE_FILES:
        if not os.path.exists(os.path.join(GENRES, name)):
            report(f"缺少 writing/genres/{name}")

    counts = {}
    checks = [("dialogue.md", check_dialogue, "条手法"), ("devices.md", check_devices, "个技巧"),
              ("doctor.md", check_doctor, "个症状"), ("intent.md", check_intent, "种效果")]
    for name, fn, unit in checks:
        path = os.path.join(WRITING, name)
        if os.path.exists(path):
            counts[name] = fn(path)
            print(f"[ok] {name}: {counts[name]} {unit}")

    gindex = os.path.join(GENRES, "index.md")
    listed = set()
    if os.path.exists(gindex):
        listed = set(re.findall(r"`([a-z-]+\.md)`", read(gindex))) - {"index.md"}
    actual = {os.path.basename(f) for f in glob.glob(os.path.join(GENRES, "*.md"))} - {"index.md"}
    for name in sorted(actual - listed):
        report(f"genres/{name} 没有列进 genres/index.md")
    for name in sorted(actual):
        check_genre(os.path.join(GENRES, name))
    print(f"[ok] genres: {len(actual)} 个类型")

    sources = os.path.join(WRITING, "sources.md")
    if os.path.exists(sources):
        text = read(sources)
        for sec in SOURCE_SECTIONS:
            if sec not in text:
                report(f"writing/sources.md: 缺小节「{sec}」")

    example = os.path.join(WRITING, "example.md")
    if os.path.exists(example) and "```text" not in read(example):
        report("writing/example.md: 没有剧本代码块")

    if os.path.exists(TEMPLATE):
        text = read(TEMPLATE)
        for sec in TEMPLATE_SECTIONS:
            if sec not in text:
                report(f"templates/script.md: 缺小节「{sec}」")
    else:
        report("缺少 templates/script.md")

    for path in sorted(glob.glob(os.path.join(WRITING, "**", "*.md"), recursive=True)):
        check_common(path)

    skill = read(os.path.join(SKILL, "SKILL.md"))
    for route in ROUTES:
        if route not in skill:
            report(f"SKILL.md 没有指向 {route}")

    total = sum(counts.values())
    print(f"\nChecked writing layer: {total} entries, {len(actual)} genres, {issues} issues.")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
