from pathlib import Path

WORKSPACE_DIR = Path("C:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")
INDEX_PATH = WORKSPACE_DIR / "index.html"
EXAM_JS_PATH = WORKSPACE_DIR / "course_exam_engine.js"

print("--- Integrity Verification ---")
print(f"Checking index.html: Exists = {INDEX_PATH.exists()}, Size = {INDEX_PATH.stat().st_size if INDEX_PATH.exists() else 0} bytes")
print(f"Checking course_exam_engine.js: Exists = {EXAM_JS_PATH.exists()}, Size = {EXAM_JS_PATH.stat().st_size if EXAM_JS_PATH.exists() else 0} bytes")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(EXAM_JS_PATH, "r", encoding="utf-8") as f:
    js_content = f.read()

checks = {
    "nav-course (Sidebar Link)": 'id="nav-course"' in html_content,
    "tab-course (Course View)": 'id="tab-course"' in html_content,
    "Target Email (abhineetsam2027@gmail.com)": 'abhineetsam2027@gmail.com' in html_content,
    "Level 1 Foundation Exam": "launchExam('level1')" in html_content or "launchExam('level1')" in js_content,
    "Grand Master Exam": "launchExam('final')" in html_content,
    "Exam Script Link": 'src="course_exam_engine.js"' in html_content
}

for check_name, status in checks.items():
    print(f"  [{'PASS' if status else 'FAIL'}] {check_name}")

print("\nVerification Complete.")
