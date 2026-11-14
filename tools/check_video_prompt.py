#!/usr/bin/env python3
"""Check the video-prompt layer: files, section and lexicon fields, worked prompts (shot counts, timecodes,
CRITICAL budget, locks, lips), template, references, routing, and alignment with aigc/prompt-syntax."""

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
VP = os.path.join(REFS, "video-prompt")
TEMPLATES = os.path.join(SKILL, "templates")

REQUIRED = ["index.md", "anatomy.md", "compile.md", "camera-behavior.md", "acting.md", "physics.md",
            "audio.md", "locks.md", "one-take.md", "example.md", "scene-prompts.md", "sources.md"]
ANATOMY_FIELDS = ["**作用**", "**写法**", "**例**", "**什么时候省**", "**常见错误**"]
ANATOMY_COUNT = 19
LEXICONS = ["camera-behavior.md", "acting.md", "physics.md", "audio.md", "locks.md", "one-take.md"]
LEXICON_FIELDS = ["**写法**", "**防什么误读**", "**用在**", "**别这样写**"]
PROMPT_FILES = ["compile.md", "example.md", "scene-prompts.md"]
CRITICAL_MAX = 3
LOCKS_MAX = 8
TEMPLATE_SECTIONS = ["## 全片层", "## 场景层", "## 单位层", "### 生成单位", "### 预判误读", "### 提示词", "### 自检"]
BANNED = ["演员", "排练", "选角", "剧组", "通告", "灯具", "轨道", "布光", "现场录音", "同期声"]
ROUTES = ["references/video-prompt/compile.md", "references/video-prompt/anatomy.md",
          "references/video-prompt/index.md", "templates/video-prompt.md",
          "camera-behavior.md", "acting.md", "physics.md", "audio.md", "locks.md", "one-take.md"]
SYNTAX_MUST = ["识别特征锁", "references/video-prompt/"]
SYNTAX_MUST_NOT = ["不重复外貌"]

REF = re.compile(r"`((?:references|templates|craft|camera|writing|storyboard|recipes|directors|"
                 r"cinematographers|aigc|drama|video-prompt)/[^`*<>\s]+?\.md)")
BARE = re.compile(r"`([a-z][a-z0-9-]*\.md)`")
BLOCK = re.compile(r"^```text\n(.*?)^```", re.M | re.S)
EDIT = re.compile(r"EDIT: (\d+) shots?, ([\d.]+) seconds")
SPAN = re.compile(r"Shot (\d+) ([\d.]+)–([\d.]+)s")
SHOT = re.compile(r"^SHOT (\d+) — ([\d.]+)–([\d.]+)s", re.M)

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
    bases = [SKILL, REFS, VP, os.path.dirname(here)]
    return any(os.path.exists(os.path.join(b, ref)) for b in bases)


def entries(text: str):
    """Yield (title, body) for each ### entry, stopping at the next ## or # heading."""
    parts = re.split(r"^### +(.+)$", text, flags=re.M)
    for i in range(1, len(parts), 2):
        body = re.split(r"^##? ", parts[i + 1], maxsplit=1, flags=re.M)[0]
        yield parts[i].strip(), body


def check_fields(path: str, fields) -> int:
    n = 0
    for title, body in entries(read(path)):
        n += 1
        for field in fields:
            if field not in body:
                report(f"{rel(path)} · {title}: 缺 {field}")
    return n


def check_prompt(path: str, label: str, block: str) -> None:
    """Validate one full multi-shot prompt (a text block that opens with an EDIT line listing shots)."""
    m = EDIT.search(block)
    shots, total = int(m.group(1)), float(m.group(2))
    spans = [(int(a), float(b), float(c)) for a, b, c in SPAN.findall(block.split("\n\n", 1)[0])]
    if len(spans) != shots:
        report(f"{rel(path)} · {label}: EDIT 写 {shots} 镜，时间码列了 {len(spans)} 段")
    t = 0.0
    for k, (num, start, end) in enumerate(spans, 1):
        if num != k:
            report(f"{rel(path)} · {label}: Shot {num} 编号不连续")
        if abs(start - t) > 1e-6 or end <= start:
            report(f"{rel(path)} · {label}: Shot {num} 时间码 {start}–{end} 不接上一镜")
        t = end
    if spans and abs(t - total) > 1e-6:
        report(f"{rel(path)} · {label}: 时间码到 {t}s，总时长写的是 {total}s")
    heads = [(int(a), float(b), float(c)) for a, b, c in SHOT.findall(block)]
    if heads and heads != spans:
        report(f"{rel(path)} · {label}: 逐镜 SHOT 标题的时间码和 EDIT 不一致")
    critical = block.count("CRITICAL")
    if critical > CRITICAL_MAX:
        report(f"{rel(path)} · {label}: CRITICAL {critical} 处，超过 {CRITICAL_MAX}")
    locks = re.search(r"^LOCKS:\n((?:- .*\n?)+)", block, re.M)
    if locks and len(locks.group(1).strip().splitlines()) > LOCKS_MAX:
        report(f"{rel(path)} · {label}: 总锁超过 {LOCKS_MAX} 条")
    for part in re.split(r"^(?=SHOT \d+ — )", block, flags=re.M)[1:]:
        if re.search(r"\bsays\b", part) and "lips" not in part:
            report(f"{rel(path)} · {label} · {part.splitlines()[0]}: 有台词但没写谁的嘴动 / 闭着")


def check_prompts(path: str) -> int:
    n = 0
    for i, block in enumerate(BLOCK.findall(read(path)), 1):
        if EDIT.search(block):
            n += 1
            check_prompt(path, f"第 {i} 个提示词块", block)
    return n


def check_common(path: str) -> None:
    text = read(path)
    if os.path.basename(path) != "sources.md" and "video-prompt/sources.md" not in text:
        report(f"{rel(path)}: 来源没有指向 video-prompt/sources.md")
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
        if not os.path.exists(os.path.join(VP, name)):
            report(f"缺少 video-prompt/{name}")

    index = os.path.join(VP, "index.md")
    if os.path.exists(index):
        listed = set(re.findall(r"`([a-z-]+\.md)`", read(index)))
        actual = {os.path.basename(f) for f in glob.glob(os.path.join(VP, "*.md"))} - {"index.md"}
        for name in sorted(actual - listed):
            report(f"video-prompt/{name} 没有列进 video-prompt/index.md")

    path = os.path.join(VP, "anatomy.md")
    if os.path.exists(path):
        n = check_fields(path, ANATOMY_FIELDS)
        if n != ANATOMY_COUNT:
            report(f"video-prompt/anatomy.md: {n} 个段落，应为 {ANATOMY_COUNT}")
        print(f"[ok] anatomy.md: {n} 个段落")

    n_entries = 0
    for name in LEXICONS:
        path = os.path.join(VP, name)
        if os.path.exists(path):
            n = check_fields(path, LEXICON_FIELDS)
            n_entries += n
            print(f"[ok] {name}: {n} 条")

    n_prompts = 0
    for name in PROMPT_FILES:
        path = os.path.join(VP, name)
        if os.path.exists(path):
            n = check_prompts(path)
            n_prompts += n
            print(f"[ok] {name}: {n} 条多镜头提示词")

    sources = os.path.join(VP, "sources.md")
    if os.path.exists(sources):
        text = read(sources)
        for name in REQUIRED:
            if name != "sources.md" and "## " + name[:-3] not in text:
                report(f"video-prompt/sources.md: 缺小节「## {name[:-3]}」")

    template = os.path.join(TEMPLATES, "video-prompt.md")
    if not os.path.exists(template):
        report("缺少 templates/video-prompt.md")
    else:
        text = read(template)
        for sec in TEMPLATE_SECTIONS:
            if sec not in text:
                report(f"templates/video-prompt.md: 缺小节「{sec}」")

    for path in sorted(glob.glob(os.path.join(VP, "*.md"))):
        check_common(path)

    skill = read(os.path.join(SKILL, "SKILL.md"))
    for route in ROUTES:
        if route not in skill:
            report(f"SKILL.md 没有指向 {route}")

    syntax = read(os.path.join(REFS, "aigc", "prompt-syntax.md"))
    for phrase in SYNTAX_MUST:
        if phrase not in syntax:
            report(f"aigc/prompt-syntax.md 没有「{phrase}」，与视频提示词层的写法原则未对齐")
    for phrase in SYNTAX_MUST_NOT:
        if phrase in syntax:
            report(f"aigc/prompt-syntax.md 仍写着「{phrase}」，与识别特征锁原则冲突")

    print(f"\nChecked video-prompt layer: {n_entries} lexicon entries, {n_prompts} multi-shot prompts, {issues} issues.")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
