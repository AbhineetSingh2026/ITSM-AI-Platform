import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

print("--- Testing All 12 Chapters & Video Studio Handlers ---")
for i in range(1, 13):
    has_ch = f'chapterNum: {i}' in html or f'chapterNum:{i}' in html or f'ch_{i}' in html
    print(f"Chapter {i}: Registered = {has_ch}")

has_player = 'id="ch-studio-video-container"' in html
has_iframe_logic = 'videoContainer.innerHTML =' in html
alerts_count = len(re.findall(r'alert\(', html))

print("\nVideo Studio Container Present:", has_player)
print("Iframe Player Injection Logic Present:", has_iframe_logic)
print("Total alert() popups remaining in index.html:", alerts_count)
