import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# Extract script 2
m = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
if len(m) >= 2:
    script_2 = m[1]
    lines = script_2.split('\n')
    balance = 0
    for idx, line in enumerate(lines, 1):
        for char in line:
            if char == '{':
                balance += 1
            elif char == '}':
                balance -= 1
                if balance < 0:
                    print(f"Extra closing brace FOUND on line {idx}: {line.strip()}")
                    balance = 0
    print("Final brace balance:", balance)
