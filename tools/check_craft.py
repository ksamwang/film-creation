#!/usr/bin/env python3
"""Check the deep craft module structure and lengths."""

import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRAFT = os.path.join(ROOT, ".claude", "skills", "film-creation", "references", "craft")
MODULES = ["story", "visual", "staging", "performance", "sound", "production"]
CJK = re.compile(r"[一-鿿]")


def chars(path: str) -> int:
    return len(CJK.findall(open(path, encoding="utf-8").read()))


def main() -> None:
    issues = 0
    if not os.path.exists(os.path.join(CRAFT, "index.md")):
        print("[!] missing craft/index.md")
        issues += 1
    if not os.path.exists(os.path.join(CRAFT, "sources.md")):
        print("[!] missing craft/sources.md")
        issues += 1

    for m in MODULES:
        d = os.path.join(CRAFT, m)
        index = os.path.join(d, "index.md")
        if not os.path.exists(index):
            print(f"[!] {m}: missing index.md")
            issues += 1
            continue
        idx_chars = chars(index)
        if not (400 <= idx_chars <= 1200):
            print(f"[!] {m}/index.md: {idx_chars} 字")
            issues += 1

        subs = [f for f in sorted(glob.glob(os.path.join(d, "*.md")))
                if os.path.basename(f) not in ("index.md", "_sources.md")]
        if not (4 <= len(subs) <= 6):
            print(f"[!] {m}: {len(subs)} 个子文件（应 4–6）")
            issues += 1
        total = 0
        for f in subs:
            n = chars(f)
            total += n
            name = os.path.basename(f)
            text = open(f, encoding="utf-8").read()
            if not (700 <= n <= 1600):
                print(f"[!] {m}/{name}: {n} 字")
                issues += 1
            if "来源" not in text:
                print(f"[!] {m}/{name}: 缺来源行")
                issues += 1
        if not (3500 <= total <= 6500):
            print(f"[!] {m}: 子文件合计 {total} 字（应 3500–6500）")
            issues += 1
        else:
            print(f"[ok] {m}: {len(subs)} 个子文件，合计 {total} 字")

    print(f"\nChecked {len(MODULES)} modules, {issues} with issues.")


if __name__ == "__main__":
    main()
