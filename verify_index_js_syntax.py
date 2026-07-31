import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# Extract all <script> blocks
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(f"Extracted {len(scripts)} inline script blocks.")

for i, s in enumerate(scripts):
    # Basic brace balance check
    opens = s.count('{')
    closes = s.count('}')
    print(f"Script {i+1}: Length = {len(s)} chars, {{ = {opens}, }} = {closes}, Balanced = {opens == closes}")

# Verify key functions exist in script
key_funcs = [
    'switchTab', 'selectCourseTrack', 'renderPlatformCourseChapters', 
    'filterCourseLevel', 'openChapterLessonModalByNum', 'closeChapterStudioModal',
    'updateDashboardMetrics', 'switchSandboxTool', 'runTicketSummarizer',
    'runCTICategorizer', 'runRCAGenerator', 'runPredictor', 'runSentimentAnalyzer',
    'calculateWatermelonIndex'
]

print("\n--- Verifying Function Implementations ---")
for fn in key_funcs:
    present = f'function {fn}' in html or f'{fn} = function' in html
    print(f"  function {fn}(): {'[EXISTS]' if present else '[MISSING]'}")
