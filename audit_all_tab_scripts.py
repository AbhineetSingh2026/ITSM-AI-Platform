import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

print("--- Checking all tabs in index.html ---")
tabs = re.findall(r'<section id="(tab-[^"]+)"[^>]*>', html)
for t in tabs:
    print("Tab Section:", t)

print("\n--- Checking all inline onclick / function calls in index.html ---")
onclicks = set(re.findall(r'onclick="([^"]+)"', html))
for c in sorted(onclicks):
    print("  onclick:", c)

print("\n--- Checking all function definitions in inline scripts ---")
funcs = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html))
for f in sorted(funcs):
    print("  defined function:", f)

missing = []
for c in onclicks:
    # extract function name before (
    m = re.match(r'([a-zA-Z0-9_]+)', c)
    if m:
        fname = m.group(1)
        if fname not in funcs and fname not in ['window', 'alert', 'console', 'location', 'history']:
            missing.append((fname, c))

print("\n--- Potentially Missing JavaScript Functions ---")
for fname, full_call in set(missing):
    print(f"  MISSING: {fname}() -> call site: onclick=\"{full_call}\"")
