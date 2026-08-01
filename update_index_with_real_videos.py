import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# Map of chapter levels to real local MP4 video files and posters
video_modal_js = """
    function openChapterLessonModalByNum(chNum) {
      const ch = platformCourseChapters.find(c => c.chapterNum === chNum);
      if (!ch) return;

      const modal = document.getElementById('chapter-studio-modal');
      const badge = document.getElementById('ch-studio-level-badge');
      const title = document.getElementById('ch-studio-title');
      const duration = document.getElementById('ch-studio-duration');
      const desc = document.getElementById('ch-studio-desc');
      const takeaways = document.getElementById('ch-studio-takeaways');
      const videoContainer = document.getElementById('ch-studio-video-container');

      if (badge) badge.textContent = ch.levelName.toUpperCase();
      if (title) title.textContent = `Chapter ${ch.chapterNum}: ${ch.title}`;
      if (duration) duration.innerHTML = `<i class="fa-regular fa-clock"></i> ${ch.duration}`;
      if (desc) desc.textContent = ch.desc;

      if (takeaways) {
        takeaways.innerHTML = ch.keyTakeaways.map(t => `<li class="flex items-start gap-2"><i class="fa-solid fa-circle-check text-emerald-400 mt-1 text-[10px]"></i> <span>${t}</span></li>`).join('');
      }

      // Load Real Local MP4 Video Player (Abhineet's actual YouTube videos)
      if (videoContainer) {
        let streamSrc = "assets/videos/video_1.mp4";
        let posterImg = "assets/yt_thumb_1.png";

        if (ch.level === 2) {
          streamSrc = "assets/videos/video_2.mp4";
          posterImg = "assets/yt_thumb_2.png";
        } else if (ch.level === 3) {
          streamSrc = "assets/videos/video_3.mp4";
          posterImg = "assets/yt_thumb_3.png";
        }
        
        videoContainer.innerHTML = `
          <video controls autoplay playsinline class="w-full h-full object-cover rounded-2xl shadow-2xl" poster="${posterImg}">
            <source src="${streamSrc}" type="video/mp4">
            Your browser does not support HTML5 video playback.
          </video>`;
      }

      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        setTimeout(() => modal.classList.remove('opacity-0'), 10);
      }
    }
"""

# Replace openChapterLessonModalByNum in index.html
html = re.sub(
    r'function openChapterLessonModalByNum\(chNum\).*?function closeChapterStudioModal\(\)',
    video_modal_js.strip() + "\n\n    function closeChapterStudioModal()",
    html,
    flags=re.DOTALL
)

index_path.write_text(html, encoding="utf-8")
print("[OK] Updated index.html with Abhineet's real MP4 video playback handlers!")
