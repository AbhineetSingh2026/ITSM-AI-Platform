import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# Update level filter buttons in index.html to include Level 4
old_filter_bar = """<button onclick="filterCourseLevel('all')" id="btn-lvl-all" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-amber-500 text-white shadow-lg shadow-amber-500/25">All Chapters (12)</button>
                <button onclick="filterCourseLevel('1')" id="btn-lvl-1" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 1: Foundation (4)</button>
                <button onclick="filterCourseLevel('2')" id="btn-lvl-2" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 2: Intermediate (4)</button>
                <button onclick="filterCourseLevel('3')" id="btn-lvl-3" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 3: Advanced ITIL & AI (4)</button>"""

new_filter_bar = """<button onclick="filterCourseLevel('all')" id="btn-lvl-all" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-amber-500 text-white shadow-lg shadow-amber-500/25">All Chapters (16)</button>
                <button onclick="filterCourseLevel('1')" id="btn-lvl-1" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 1: Foundation (4)</button>
                <button onclick="filterCourseLevel('2')" id="btn-lvl-2" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 2: Practitioner (4)</button>
                <button onclick="filterCourseLevel('3')" id="btn-lvl-3" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 3: Advanced Analyst (4)</button>
                <button onclick="filterCourseLevel('4')" id="btn-lvl-4" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 4: Lead Practitioner (4)</button>"""

if 'btn-lvl-4' not in html:
    html = html.replace(old_filter_bar, new_filter_bar)

# Link course_curriculum_engine.js before body end
if 'course_curriculum_engine.js' not in html:
    html = html.replace('</body>', '  <script src="course_curriculum_engine.js"></script>\n</body>')

index_path.write_text(html, encoding="utf-8")
print("[OK] Updated index.html with 16-Module Level 1-4 filter buttons & course_curriculum_engine.js script tag!")
