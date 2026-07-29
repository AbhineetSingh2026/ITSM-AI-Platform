import re
from pathlib import Path

# Paths
STEP_CONTENT_PATH = Path(r"C:\Users\abhin\.gemini\antigravity-ide\brain\7663fe4b-72f0-4a4e-8941-bc7b52daff07\.system_generated\steps\224\content.md")
TARGET_DIR = Path(r"C:\ANTIGRAVITY_ABHINEET\MY WORKSPACE\itsm-ai-platform")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

INDEX_HTML_PATH = TARGET_DIR / "index.html"

# Read step 224 content
with open(STEP_CONTENT_PATH, "r", encoding="utf-8") as f:
    raw_file = f.read()

# Extract HTML content starting from <!DOCTYPE html>
match = re.search(r"(<!DOCTYPE html>.*)", raw_file, re.DOTALL)
if not match:
    print("Error: Could not find <!DOCTYPE html> in step 224 content.")
    exit(1)

html = match.group(1)

print(f"Extracted raw HTML from step 224 content ({len(html)} characters).")
