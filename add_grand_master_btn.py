import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# Add Grand Master Exam button into the sd-ops track header
grand_master_btn_html = """<div class="flex flex-wrap items-center justify-between gap-4 p-4 glass-panel border border-amber-400/30 rounded-2xl bg-amber-500/5 mb-6">
            <div>
              <h4 class="font-bold text-white text-sm">IT Service Desk Grand Master Certification</h4>
              <p class="text-slate-400 text-xs mt-0.5">Comprehensive 50-Question Scenario Examination covering Level 1, 2, and 3 Modules.</p>
            </div>
            <button onclick="launchExam('final')" class="cyber-btn bg-gradient-to-r from-amber-500 via-emerald-500 to-cyberPurple text-white font-bold py-2.5 px-6 rounded-xl shadow-lg hover:scale-105 transition"><i class="fa-solid fa-trophy text-amber-300"></i> Grand Master Exam (50 Qs)</button>
          </div>"""

if "launchExam('final')" not in html:
  html = html.replace(
      '<div id="course-track-sd-ops-view" class="space-y-8">',
      '<div id="course-track-sd-ops-view" class="space-y-8">\n'
      + grand_master_btn_html,
  )

index_path.write_text(html, encoding="utf-8")
print(
    "[OK] Added Grand Master Exam button to IT Service Desk Operations track!"
)
