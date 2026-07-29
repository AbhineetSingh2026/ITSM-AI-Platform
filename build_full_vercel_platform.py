import re
from pathlib import Path

WORKSPACE_DIR = Path("C:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")
WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)

STEP_CONTENT_PATH = Path(r"C:\Users\abhin\.gemini\antigravity-ide\brain\7663fe4b-72f0-4a4e-8941-bc7b52daff07\.system_generated\steps\224\content.md")

with open(STEP_CONTENT_PATH, "r", encoding="utf-8") as f:
    raw_file = f.read()

match = re.search(r"(<!DOCTYPE html>.*)", raw_file, re.DOTALL)
if not match:
    print("Error: Could not extract HTML.")
    exit(1)

html = match.group(1)

# 1. Inject Course Nav in Sidebar
sidebar_nav_target = '<a href="#" onclick="switchTab(\'services\')" id="nav-services" class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white transition-all text-sm font-semibold border-l-3 border-transparent">\n            <i class="fa-solid fa-screwdriver-wrench text-base"></i> Services\n          </a>'

course_nav_sidebar = """<a href="#" onclick="switchTab('services')" id="nav-services" class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white transition-all text-sm font-semibold border-l-3 border-transparent">
            <i class="fa-solid fa-screwdriver-wrench text-base"></i> Services
          </a>
          <a href="#" onclick="switchTab('course')" id="nav-course" class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white transition-all text-sm font-semibold border-l-3 border-transparent">
            <i class="fa-solid fa-graduation-cap text-base text-amber-400"></i> Service Desk Course <span class="px-1.5 py-0.5 text-[9px] font-extrabold bg-amber-400/20 text-amber-400 border border-amber-400/30 rounded-md uppercase ml-auto">Free</span>
          </a>"""

if sidebar_nav_target in html and 'id="nav-course"' not in html:
    html = html.replace(sidebar_nav_target, course_nav_sidebar)

# 2. Inject Course Nav in Mobile Overlay
mobile_nav_target = '<a href="#" onclick="switchTabMobile(\'services\')" class="text-slate-400 hover:text-cyberCyan transition-all">Services</a>'
mobile_nav_course = '<a href="#" onclick="switchTabMobile(\'services\')" class="text-slate-400 hover:text-cyberCyan transition-all">Services</a>\n      <a href="#" onclick="switchTabMobile(\'course\')" class="text-slate-400 hover:text-cyberCyan transition-all text-amber-400 font-bold flex items-center gap-2"><i class="fa-solid fa-graduation-cap"></i> Service Desk Course & Exams</a>'

if mobile_nav_target in html and 'switchTabMobile(\'course\')' not in html:
    html = html.replace(mobile_nav_target, mobile_nav_course)

# 3. Add tab-course Section HTML
course_section_html = """
      <!-- ==================== SERVICE DESK COURSE & EXAMS TAB ==================== -->
      <section id="tab-course" class="tab-view hidden space-y-8 max-w-6xl mx-auto">
        <!-- Hero Course Banner -->
        <div class="glass-panel p-6 md:p-10 relative overflow-hidden flex flex-col lg:flex-row items-center justify-between gap-8 bg-gradient-to-br from-cyberSlate to-cyberBg">
          <div class="space-y-4 flex-1">
            <span class="badge-neon"><i class="fa-solid fa-graduation-cap text-amber-400"></i> Free 12-Chapter Certification Curriculum</span>
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold tracking-tight text-white leading-tight">
              IT Service Desk & <span class="bg-clip-text text-transparent bg-gradient-to-r from-amber-400 via-cyberCyan to-cyberPurple">AI Operations Mastery</span>
            </h1>
            <p class="text-slate-300 text-sm leading-relaxed max-w-2xl">
              Master IT Helpdesk Fundamentals, Advanced ITSM Operations, and Next-Gen AI Virtual Agent Automation — structured step-by-step into 3 Skill Progression Levels with automated exams and official certification.
            </p>
            <div class="flex flex-wrap gap-3 pt-2">
              <button onclick="launchExam('final')" class="cyber-btn bg-gradient-to-r from-emerald-500 to-cyberPurple"><i class="fa-solid fa-trophy"></i> Grand Master Exam (50 Qs)</button>
              <div onclick="copyDirectEmail()" class="glass-panel px-4 py-2 border.border-white/[0.1] rounded-xl flex items-center gap-2 text-xs font-mono font-bold text-white cursor-pointer hover:border-amber-400 transition" title="Click to copy email">
                <i class="fa-solid fa-envelope text-amber-400"></i> abhineetsam2027@gmail.com <i class="fa-solid fa-copy text-slate-500"></i>
              </div>
            </div>
          </div>
          <!-- Stats Badge -->
          <div class="flex gap-4 shrink-0 font-mono">
            <div class="p-4 glass-panel border border-white/[0.08] rounded-2xl text-center min-w-[90px]">
              <span class="text-3xl font-extrabold text-white block">3</span>
              <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Levels</span>
            </div>
            <div class="p-4 glass-panel border border-white/[0.08] rounded-2xl text-center min-w-[90px]">
              <span class="text-3xl font-extrabold text-cyberCyan block">12</span>
              <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Chapters</span>
            </div>
            <div class="p-4 glass-panel border border-white/[0.08] rounded-2xl text-center min-w-[90px]">
              <span class="text-3xl font-extrabold text-emerald-400 block">100%</span>
              <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Free</span>
            </div>
          </div>
        </div>

        <!-- Level Filter Tabs -->
        <div class="flex gap-3 overflow-x-auto pb-2 border-b border-white/[0.08]">
          <button onclick="filterCourseLevel('all')" id="btn-lvl-all" class="course-lvl-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all bg-amber-500 text-white shadow-lg shadow-amber-500/25">All Chapters (12)</button>
          <button onclick="filterCourseLevel('1')" id="btn-lvl-1" class="course-lvl-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all bg-white/[0.03] text-slate-400 hover:text-white border border-white/[0.08]">Level 1: Foundation (4)</button>
          <button onclick="filterCourseLevel('2')" id="btn-lvl-2" class="course-lvl-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all bg-white/[0.03] text-slate-400 hover:text-white border border-white/[0.08]">Level 2: Intermediate (4)</button>
          <button onclick="filterCourseLevel('3')" id="btn-lvl-3" class="course-lvl-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all bg-white/[0.03] text-slate-400 hover:text-white border border-white/[0.08]">Level 3: Advanced ITIL & AI (4)</button>
        </div>

        <!-- Level Summaries Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="glass-panel p-6 border-t-4 border-emerald-500 space-y-3">
            <div class="flex justify-between items-center text-xs">
              <span class="px-2.5 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 uppercase">Level 1: Foundation</span>
              <span class="text-slate-500 font-mono text-[10px]">Chapters 1–4</span>
            </div>
            <h3 class="text-base font-bold text-white">Helpdesk Basics & L1 Operations</h3>
            <p class="text-slate-400 text-xs leading-relaxed">Master ticket logging, priority matrices, Active Directory password resets, SLA clocks, and user communication skills.</p>
            <button onclick="launchExam('level1')" class="w-full py-2 bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 rounded-xl text-emerald-400 text-xs font-bold transition"><i class="fa-solid fa-pen-to-square"></i> Take Level 1 Exam (20 Qs)</button>
          </div>

          <div class="glass-panel p-6 border-t-4 border-cyberBlue space-y-3">
            <div class="flex justify-between items-center text-xs">
              <span class="px-2.5 py-0.5 rounded text-[10px] font-bold bg-cyberBlue/20 text-cyberBlue border border-cyberBlue/30 uppercase">Level 2: Intermediate</span>
              <span class="text-slate-500 font-mono text-[10px]">Chapters 5–8</span>
            </div>
            <h3 class="text-base font-bold text-white">ITSM Operations, Intune & JML</h3>
            <p class="text-slate-400 text-xs leading-relaxed">Deep dive into Microsoft Intune endpoint management, VDI, NHS Smartcard RA administration, Major Incident bridges, and CAB approvals.</p>
            <button onclick="launchExam('level2')" class="w-full py-2 bg-cyberBlue/10 hover:bg-cyberBlue/20 border border-cyberBlue/30 rounded-xl text-cyberBlue text-xs font-bold transition"><i class="fa-solid fa-pen-to-square"></i> Take Level 2 Exam (30 Qs)</button>
          </div>

          <div class="glass-panel p-6 border-t-4 border-cyberPurple space-y-3">
            <div class="flex justify-between items-center text-xs">
              <span class="px-2.5 py-0.5 rounded text-[10px] font-bold bg-cyberPurple/20 text-cyberPurple border border-cyberPurple/30 uppercase">Level 3: Advanced</span>
              <span class="text-slate-500 font-mono text-[10px]">Chapters 9–12</span>
            </div>
            <h3 class="text-base font-bold text-white">ITIL Management, XLAs & AI Agents</h3>
            <p class="text-slate-400 text-xs leading-relaxed">Implement Shift-Left self-service, Experience Level Agreements (XLAs), ServiceNow/Halo ESM workflows, and AI Virtual Agent automation.</p>
            <button onclick="launchExam('level3')" class="w-full py-2 bg-cyberPurple/10 hover:bg-cyberPurple/20 border border-cyberPurple/30 rounded-xl text-cyberPurple text-xs font-bold transition"><i class="fa-solid fa-pen-to-square"></i> Take Level 3 Exam (40 Qs)</button>
          </div>
        </div>

        <!-- Master Exam Banner Callout -->
        <div class="glass-panel p-6 border border-amber-500/30 bg-gradient-to-r from-amber-500/10 via-cyberPurple/10 to-transparent flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="space-y-1">
            <span class="text-[10px] font-bold text-amber-400 uppercase tracking-widest"><i class="fa-solid fa-award"></i> FINAL VERIFIED CERTIFICATION</span>
            <h3 class="text-xl font-bold text-white">Grand Master Certification Exam (50 Questions | 100 Marks)</h3>
            <p class="text-xs text-slate-300">Score 70% or higher to generate an official printable Certificate of Completion signed by Abhineet Singh.</p>
          </div>
          <button onclick="launchExam('final')" class="cyber-btn bg-gradient-to-r from-amber-500 to-cyberPurple text-white shrink-0"><i class="fa-solid fa-trophy"></i> Start Master Exam & Get Certified</button>
        </div>

        <!-- Course Chapters Grid Container -->
        <div id="course-chapters-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- Dynamically populated by JS -->
        </div>
      </section>
"""

if '</main>' in html and 'id="tab-course"' not in html:
    html = html.replace('</main>', course_section_html + '\n    </main>')

# Write modified HTML
with open(WORKSPACE_DIR / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with tab-course section successfully!")
