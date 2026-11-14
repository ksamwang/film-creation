#!/usr/bin/env python3
"""Check the camera lookup layer: files, entry fields, recipe sections, references, routing."""

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
CAMERA = os.path.join(REFS, "camera")
RECIPES = os.path.join(CAMERA, "recipes")

LEXICONS = ["lexicon-shot.md", "lexicon-move.md", "lexicon-light.md", "lexicon-frame.md"]
REQUIRED = ["index.md", "intent.md", "sources.md", "lexicon-transition.md"] + LEXICONS
RECIPE_FILES = ["dialogue-two.md", "dialogue-group.md", "chase.md", "fight.md", "suspense.md",
                "romance.md", "montage.md", "opening-ending.md", "reversal.md"]
RECIPE_SECTIONS = ["## 这场戏要什么", "## 默认序列", "## 示例", "## 变体",
                   "## 竖屏 / 短剧", "## 失败与修法", "## 可借的档案", "## 来源"]
GRADES = ("稳", "定帧", "后期")
BANNED = ["演员", "排练", "选角", "剧组", "通告", "灯具", "轨道", "布光", "现场录音", "同期声"]
ROUTES = ["references/camera/index.md", "references/camera/intent.md",
          "references/camera/recipes/index.md"]
REF = re.compile(r"`((?:references|templates|craft|camera|recipes|directors|cinematographers|aigc|drama)/[^`*<>\s]+?\.md)")
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
    bases = [SKILL, REFS, CAMERA, os.path.dirname(here)]
    return any(os.path.exists(os.path.join(b, ref)) for b in bases)


def bare_resolves(name: str, here: str) -> bool:
    bases = [os.path.dirname(here), CAMERA, RECIPES,
             os.path.join(REFS, "craft", "staging"), os.path.join(REFS, "craft", "visual")]
    return any(os.path.exists(os.path.join(b, name)) for b in bases)


def entries(text: str):
    """Yield (title, body) for each ### entry."""
    parts = re.split(r"^### +(.+)$", text, flags=re.M)
    for i in range(1, len(parts), 2):
        body = re.split(r"^##? ", parts[i + 1], maxsplit=1, flags=re.M)[0]
        yield parts[i].strip(), body


def check_lexicon(path: str) -> int:
    text = read(path)
    n = 0
    for title, body in entries(text):
        if "**写法**" not in body:
            continue  # pointer entries such as「见 lexicon-shot.md」
        n += 1
        for field in ("**作用**", "**生成**"):
            if field not in body:
                report(f"{rel(path)} · {title}: 缺 {field}")
        m = re.search(r"\*\*生成\*\*：(.+)", body)
        if m and not any(g in m.group(1) for g in GRADES):
            report(f"{rel(path)} · {title}: 生成没有写分级（稳 / 定帧 / 后期）")
    return n


def check_transition(path: str) -> int:
    text = read(path)
    n = 0
    for title, body in entries(text):
        if "**生成侧**" not in body and "**剪辑侧**" not in body:
            continue
        n += 1
        if "**作用**" not in body:
            report(f"{rel(path)} · {title}: 缺 **作用**")
        m = re.search(r"\*\*生成\*\*：(.+)", body)
        if not m:
            report(f"{rel(path)} · {title}: 缺 **生成**")
        elif not any(g in m.group(1) for g in GRADES):
            report(f"{rel(path)} · {title}: 生成没有写分级（稳 / 定帧 / 后期）")
    return n


def check_recipe(path: str) -> None:
    text = read(path)
    for sec in RECIPE_SECTIONS:
        if sec not in text:
            report(f"{rel(path)}: 缺小节「{sec}」")
    if "```text" not in text:
        report(f"{rel(path)}: 没有逐镜示例代码块")
    if not re.search(r"^\| *# *\|", text, flags=re.M):
        report(f"{rel(path)}: 没有镜头表")


def check_common(path: str) -> None:
    text = read(path)
    if os.path.basename(path) != "sources.md" and "camera/sources.md" not in text:
        report(f"{rel(path)}: 来源没有指向 camera/sources.md")
    for ref in REF.findall(text):
        if not resolves(ref, path):
            report(f"{rel(path)}: 引用不存在 {ref}")
    for name in BARE.findall(text):
        if not bare_resolves(name, path):
            report(f"{rel(path)}: 引用不存在 {name}")
    for word in BANNED:
        if word in text:
            report(f"{rel(path)}: 出现实拍用语「{word}」")


def main() -> None:
    for name in REQUIRED:
        if not os.path.exists(os.path.join(CAMERA, name)):
            report(f"缺少 camera/{name}")
    if not os.path.exists(os.path.join(RECIPES, "index.md")):
        report("缺少 camera/recipes/index.md")
    for name in RECIPE_FILES:
        if not os.path.exists(os.path.join(RECIPES, name)):
            report(f"缺少 camera/recipes/{name}")

    total = 0
    for name in LEXICONS:
        path = os.path.join(CAMERA, name)
        if os.path.exists(path):
            n = check_lexicon(path)
            total += n
            print(f"[ok] {name}: {n} 个条目")
    path = os.path.join(CAMERA, "lexicon-transition.md")
    if os.path.exists(path):
        n = check_transition(path)
        total += n
        print(f"[ok] lexicon-transition.md: {n} 个条目")

    listed = set()
    rindex = os.path.join(RECIPES, "index.md")
    if os.path.exists(rindex):
        listed = set(re.findall(r"`([a-z-]+\.md)`", read(rindex))) - {"index.md"}
    actual = {os.path.basename(f) for f in glob.glob(os.path.join(RECIPES, "*.md"))} - {"index.md"}
    for name in sorted(actual - listed):
        report(f"recipes/{name} 没有列进 recipes/index.md")
    for name in sorted(actual):
        check_recipe(os.path.join(RECIPES, name))
    print(f"[ok] recipes: {len(actual)} 份配方")

    for path in sorted(glob.glob(os.path.join(CAMERA, "**", "*.md"), recursive=True)):
        check_common(path)

    skill = read(os.path.join(SKILL, "SKILL.md"))
    for route in ROUTES:
        if route not in skill:
            report(f"SKILL.md 没有指向 {route}")

    print(f"\nChecked camera layer: {total} lexicon entries, {issues} issues.")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
