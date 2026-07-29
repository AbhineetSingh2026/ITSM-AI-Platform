import shutil
from pathlib import Path

VERCEL_DIR = Path("C:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")
NETLIFY_DIST = Path("C:/ANTIGRAVITY_ABHINEET/Folkestone_Beach_Video/dist")

NETLIFY_DIST.mkdir(parents=True, exist_ok=True)

# Copy index.html, course_exam_engine.js
shutil.copy2(VERCEL_DIR / "index.html", NETLIFY_DIST / "index.html")
shutil.copy2(VERCEL_DIR / "index.html", NETLIFY_DIST / "portal.aspx")
shutil.copy2(VERCEL_DIR / "course_exam_engine.js", NETLIFY_DIST / "course_exam_engine.js")

if (VERCEL_DIR / "menu.html").exists():
    shutil.copy2(VERCEL_DIR / "menu.html", NETLIFY_DIST / "menu.html")

print("Synced index.html and course_exam_engine.js to Netlify dist/ directory successfully!")
