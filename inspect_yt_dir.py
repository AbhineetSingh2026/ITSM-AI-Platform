import os
from pathlib import Path

yt_dir = Path(r"C:\ANTIGRAVITY_ABHINEET\MY_EARNING\You tube Channel")
if yt_dir.exists():
    for root, dirs, files in os.walk(yt_dir):
        for f in files:
            p = Path(root) / f
            print(f"{p.relative_to(yt_dir)} ({p.stat().st_size} bytes)")
