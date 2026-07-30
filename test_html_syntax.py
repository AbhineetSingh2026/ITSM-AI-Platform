import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

print("HTML Length:", len(html), "bytes")
print("Number of script tags:", len(re.findall(r'<script', html)))
print("Number of section tags:", len(re.findall(r'<section', html)))
print("Number of modal divs:", len(re.findall(r'modal', html)))
