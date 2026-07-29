import shutil
from pathlib import Path

SRC_JS = Path("C:/ANTIGRAVITY_ABHINEET/Folkestone_Beach_Video/static/js/course_exam_engine.js")
DEST_DIR = Path("C:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")
DEST_JS = DEST_DIR / "course_exam_engine.js"

shutil.copy2(SRC_JS, DEST_JS)
print(f"Copied course_exam_engine.js to {DEST_JS}")

INDEX_PATH = DEST_DIR / "index.html"
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

tag = '<script src="course_exam_engine.js"></script>'
if tag not in html:
    html = html.replace('</body>', f'{tag}\n</body>')

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Linked course_exam_engine.js into index.html successfully!")
