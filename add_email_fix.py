import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# Add contact email to hero / contact section
if "abhineetsam2027@gmail.com" not in html:
    html = html.replace(
        'Book Consultation / Contact Abhineet',
        'Book Consultation / Contact Abhineet (<span class="text-cyberCyan">abhineetsam2027@gmail.com</span>)'
    )

index_path.write_text(html, encoding="utf-8")
print("[OK] Added target email to index.html!")
