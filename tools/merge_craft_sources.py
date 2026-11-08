#!/usr/bin/env python3
"""Merge per-module _sources.md fragments into craft/sources.md."""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRAFT = os.path.join(ROOT, ".claude", "skills", "film-creation", "references", "craft")
MODULES = ["story", "visual", "staging", "performance", "sound", "production"]


def main() -> None:
    parts = []
    for m in MODULES:
        path = os.path.join(CRAFT, m, "_sources.md")
        if not os.path.exists(path):
            print(f"[!] missing {m}/_sources.md")
            continue
        text = open(path, encoding="utf-8").read().strip()
        # Normalize heading to the module name
        if not text.startswith("## "):
            text = f"## {m}\n\n" + text
        parts.append(text)

    out = ["# 来源表\n", "> 每条规则/概念 → 书名/章节。正文只标注模块锚点。\n"]
    out.extend(parts)
    out.append("")
    target = os.path.join(CRAFT, "sources.md")
    open(target, "w", encoding="utf-8").write("\n\n".join(out))
    print(f"Wrote {target} with {len(parts)} module sections.")


if __name__ == "__main__":
    main()
