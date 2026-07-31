import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# Duplicate block to remove
dup_block = """      if (modal) {
        modal.classList.add('opacity-0');
        setTimeout(() => {
          modal.classList.add('hidden');
          modal.classList.remove('flex');
        }, 300);
      }
    }"""

if dup_block in html:
    html = html.replace(dup_block, '', 1)
    print("[OK] Removed duplicate block from script 2!")
else:
    # Use regex replacement to ensure clean syntax
    html = re.sub(
        r'function closeChapterStudioModal\(\)\s*\{.*?\n\s*\}\s*if \(modal\) \{.*?\n\s*\}',
        '''function closeChapterStudioModal() {
      const modal = document.getElementById('chapter-studio-modal');
      const videoContainer = document.getElementById('ch-studio-video-container');
      if (videoContainer) {
        videoContainer.innerHTML = '';
      }
      if (modal) {
        modal.classList.add('opacity-0');
        setTimeout(() => {
          modal.classList.add('hidden');
          modal.classList.remove('flex');
        }, 300);
      }
    }''',
        html,
        flags=re.DOTALL
    )
    print("[OK] Cleaned closeChapterStudioModal function with regex!")

index_path.write_text(html, encoding="utf-8")
