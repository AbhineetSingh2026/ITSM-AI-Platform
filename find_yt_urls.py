import re
from pathlib import Path

yt_dir = Path(r"C:\ANTIGRAVITY_ABHINEET\MY_EARNING\You tube Channel")

print("--- Searching for YouTube Video IDs / Links ---")
for p in yt_dir.glob("*.md"):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    matches = re.findall(r'(https?://[^\s]+)', txt)
    if matches:
        print(f"File {p.name}:")
        for m in matches:
            print("  ", m)
