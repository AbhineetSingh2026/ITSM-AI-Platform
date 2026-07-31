from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

import re
m = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
if len(m) >= 2:
    script_2 = m[1]
    lines = script_2.split('\n')
    for i in range(175, 205):
        if i < len(lines):
            print(f"Line {i+1}: {lines[i]}")
