import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# 1. Update Sidebar Nav label: Service Desk Course -> Courses (Free)
html = re.sub(
    r'<a href="#" onclick="switchTab\(\'course\'\)" id="nav-course"[^>]*>.*?</a>',
    '''<a href="#" onclick="switchTab('course')" id="nav-course" class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white transition-all text-sm font-semibold border-l-3 border-transparent">
            <i class="fa-solid fa-graduation-cap text-base text-amber-400"></i> Courses (Free) <span class="px-1.5 py-0.5 text-[9px] font-extrabold bg-amber-400/20 text-amber-400 border border-amber-400/30 rounded-md uppercase ml-auto">Free</span>
          </a>''',
    html,
    flags=re.DOTALL
)

# 2. Update Mobile Overlay Nav label
html = re.sub(
    r'<a href="#" onclick="switchTabMobile\(\'course\'\)"[^>]*>.*?</a>',
    '<a href="#" onclick="switchTabMobile(\'course\')" class="text-slate-400 hover:text-cyberCyan transition-all text-amber-400 font-bold flex items-center gap-2"><i class="fa-solid fa-graduation-cap"></i> Courses (Free)</a>',
    html
)

# 3. Build Multi-Course Academy Tab Section
multi_course_section = """<section id="tab-course" class="tab-view hidden space-y-8 max-w-6xl mx-auto">
        <!-- Hero Course Banner -->
        <div class="glass-panel p-6 md:p-10 relative overflow-hidden flex flex-col lg:flex-row items-center justify-between gap-8 bg-gradient-to-br from-cyberSlate to-cyberBg border border-amber-500/30">
          <div class="space-y-4 flex-1">
            <span class="badge-neon border-amber-400/40 text-amber-400 bg-amber-400/10"><i class="fa-solid fa-graduation-cap text-amber-400"></i> Free Multi-Track Certification Academy</span>
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold tracking-tight text-white leading-tight">
              Global ITSM & <span class="bg-clip-text text-transparent bg-gradient-to-r from-amber-400 via-cyberCyan to-cyberPurple">AI Operations Academy</span>
            </h1>
            <p class="text-slate-300 text-sm leading-relaxed max-w-2xl">
              Select a specialized learning track below to master Service Desk Operations, Major Incident Management (MIM), IT Service Leadership, or Knowledge Base Management.
            </p>
          </div>
          <div class="flex gap-4 shrink-0 font-mono">
            <div class="p-4 glass-panel border border-white/[0.08] rounded-2xl text-center min-w-[90px]">
              <span class="text-3xl font-extrabold text-white block">4</span>
              <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Tracks</span>
            </div>
            <div class="p-4 glass-panel border border-white/[0.08] rounded-2xl text-center min-w-[90px]">
              <span class="text-3xl font-extrabold text-cyberCyan block">12+</span>
              <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Chapters</span>
            </div>
            <div class="p-4 glass-panel border border-white/[0.08] rounded-2xl text-center min-w-[90px]">
              <span class="text-3xl font-extrabold text-emerald-400 block">100%</span>
              <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Free</span>
            </div>
          </div>
        </div>

        <!-- Course Category Folder Selector Cards -->
        <div class="space-y-4">
          <h3 class="text-lg font-bold text-white uppercase tracking-wider text-xs font-mono text-slate-400 flex items-center gap-2">
            <i class="fa-solid fa-folder-open text-amber-400"></i> Select Course Track / Learning Path
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            
            <!-- Folder 1: IT Service Desk Operations (Active) -->
            <div onclick="selectCourseTrack('sd-ops')" id="track-card-sd-ops" class="course-track-card glass-panel p-5 border-2 border-amber-400 bg-amber-500/10 cursor-pointer hover:border-amber-400 transition-all rounded-2xl space-y-3 relative group">
              <div class="flex justify-between items-center">
                <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 border border-amber-400/30 flex items-center justify-center text-lg">
                  <i class="fa-solid fa-headset"></i>
                </div>
                <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-mono uppercase">12 Chapters • Active</span>
              </div>
              <div>
                <h4 class="font-bold text-sm text-white group-hover:text-amber-400 transition-colors">IT Service Desk Operations</h4>
                <p class="text-[11px] text-slate-300 mt-1 line-clamp-2">Helpdesk basics, L1-L2 troubleshooting, ticket lifecycle, AD resets, and AI triage.</p>
              </div>
              <div class="pt-1 text-[10px] text-amber-400 font-mono font-bold flex items-center gap-1">
                <span>View Full Curriculum</span> <i class="fa-solid fa-arrow-right text-xs"></i>
              </div>
            </div>

            <!-- Folder 2: Major Incident Management (MIM) (Coming Soon) -->
            <div onclick="selectCourseTrack('mim')" id="track-card-mim" class="course-track-card glass-panel p-5 border border-white/[0.08] hover:border-cyberCyan/50 cursor-pointer transition-all rounded-2xl space-y-3 relative group">
              <div class="flex justify-between items-center">
                <div class="w-10 h-10 rounded-xl bg-cyberCyan/10 text-cyberCyan border border-cyberCyan/20 flex items-center justify-center text-lg">
                  <i class="fa-solid fa-triangle-exclamation"></i>
                </div>
                <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-cyberCyan/10 text-cyberCyan border border-cyberCyan/30 font-mono uppercase">Coming Soon</span>
              </div>
              <div>
                <h4 class="font-bold text-sm text-white group-hover:text-cyberCyan transition-colors">Major Incident Management (MIM)</h4>
                <p class="text-[11px] text-slate-400 mt-1 line-clamp-2">P1 bridge call command, executive comms, 5-Why RCA templates, and CAB approvals.</p>
              </div>
              <div class="pt-1 text-[10px] text-slate-400 font-mono font-bold flex items-center gap-1 group-hover:text-cyberCyan">
                <span>Preview Syllabus</span> <i class="fa-solid fa-arrow-right text-xs"></i>
              </div>
            </div>

            <!-- Folder 3: IT Service Desk Manager (Coming Soon) -->
            <div onclick="selectCourseTrack('sd-manager')" id="track-card-sd-manager" class="course-track-card glass-panel p-5 border border-white/[0.08] hover:border-cyberPurple/50 cursor-pointer transition-all rounded-2xl space-y-3 relative group">
              <div class="flex justify-between items-center">
                <div class="w-10 h-10 rounded-xl bg-cyberPurple/10 text-cyberPurple border border-cyberPurple/20 flex items-center justify-center text-lg">
                  <i class="fa-solid fa-user-tie"></i>
                </div>
                <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-cyberPurple/10 text-cyberPurple border border-cyberPurple/30 font-mono uppercase">Coming Soon</span>
              </div>
              <div>
                <h4 class="font-bold text-sm text-white group-hover:text-cyberPurple transition-colors">IT Service Desk Manager</h4>
                <p class="text-[11px] text-slate-400 mt-1 line-clamp-2">Service Delivery leadership, SLA/XLA governance, team KPIs, and AI transformation.</p>
              </div>
              <div class="pt-1 text-[10px] text-slate-400 font-mono font-bold flex items-center gap-1 group-hover:text-cyberPurple">
                <span>Preview Syllabus</span> <i class="fa-solid fa-arrow-right text-xs"></i>
              </div>
            </div>

            <!-- Folder 4: Knowledge Base Management (Coming Soon) -->
            <div onclick="selectCourseTrack('kbm')" id="track-card-kbm" class="course-track-card glass-panel p-5 border border-white/[0.08] hover:border-emerald-400/50 cursor-pointer transition-all rounded-2xl space-y-3 relative group">
              <div class="flex justify-between items-center">
                <div class="w-10 h-10 rounded-xl bg-emerald-400/10 text-emerald-400 border border-emerald-400/20 flex items-center justify-center text-lg">
                  <i class="fa-solid fa-book-bookmark"></i>
                </div>
                <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-emerald-400/10 text-emerald-400 border border-emerald-400/30 font-mono uppercase">Coming Soon</span>
              </div>
              <div>
                <h4 class="font-bold text-sm text-white group-hover:text-emerald-400 transition-colors">Knowledge Base Management (KBM)</h4>
                <p class="text-[11px] text-slate-400 mt-1 line-clamp-2">KCS methodology, self-service portals, KB drafting, and AI indexing strategies.</p>
              </div>
              <div class="pt-1 text-[10px] text-slate-400 font-mono font-bold flex items-center gap-1 group-hover:text-emerald-400">
                <span>Preview Syllabus</span> <i class="fa-solid fa-arrow-right text-xs"></i>
              </div>
            </div>

          </div>
        </div>

        <!-- TRACK 1: IT SERVICE DESK OPERATIONS CONTENT (FULL 12 CHAPTERS & EXAMS) -->
        <div id="course-track-sd-ops-view" class="space-y-8">
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
              <h3 class="text-base font-bold text-white">SysAdmin & Enterprise Support</h3>
              <p class="text-slate-400 text-xs leading-relaxed">Hardware provisioning, Intune MDM, EMIS Web/SystmOne clinical app support, JML workflows, RA Smartcards, and CAB approvals.</p>
              <button onclick="launchExam('level2')" class="w-full py-2 bg-cyberBlue/10 hover:bg-cyberBlue/20 border border-cyberBlue/30 rounded-xl text-cyberBlue text-xs font-bold transition"><i class="fa-solid fa-pen-to-square"></i> Take Level 2 Exam (20 Qs)</button>
            </div>

            <div class="glass-panel p-6 border-t-4 border-cyberPurple space-y-3">
              <div class="flex justify-between items-center text-xs">
                <span class="px-2.5 py-0.5 rounded text-[10px] font-bold bg-cyberPurple/20 text-cyberPurple border border-cyberPurple/30 uppercase">Level 3: Advanced</span>
                <span class="text-slate-500 font-mono text-[10px]">Chapters 9–12</span>
              </div>
              <h3 class="text-base font-bold text-white">ITIL 4, XLAs & AI Operations</h3>
              <p class="text-slate-400 text-xs leading-relaxed">ITIL v4 Service Value Chain, SLA vs XLA Experience Level Agreements, Power BI reporting, and AI Copilot automated ticket triage.</p>
              <button onclick="launchExam('level3')" class="w-full py-2 bg-cyberPurple/10 hover:bg-cyberPurple/20 border border-cyberPurple/30 rounded-xl text-cyberPurple text-xs font-bold transition"><i class="fa-solid fa-pen-to-square"></i> Take Level 3 Exam (20 Qs)</button>
            </div>
          </div>
        </div>

        <!-- TRACK 2: MAJOR INCIDENT MANAGEMENT PREVIEW (COMING SOON) -->
        <div id="course-track-mim-view" class="space-y-6 hidden">
          <div class="glass-panel p-8 space-y-4 border border-cyberCyan/30 text-center">
            <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-cyberCyan/10 text-cyberCyan border border-cyberCyan/30 uppercase">Track 2: Coming Soon</span>
            <h3 class="text-2xl font-bold text-white">Major Incident Management (MIM) Masterclass</h3>
            <p class="text-slate-300 text-xs max-w-xl mx-auto leading-relaxed">
              Curriculum in active production: P1 War Room Command, Executive Stakeholder Communications, 5-Why RCA Frameworks, and Emergency CAB Governance.
            </p>
            <div class="pt-4">
              <button onclick="alert('Pre-registration recorded! We will notify you when MIM Track goes live.')" class="cyber-btn"><i class="fa-solid fa-bell"></i> Pre-Register for MIM Track (Free)</button>
            </div>
          </div>
        </div>

        <!-- TRACK 3: IT SERVICE DESK MANAGER PREVIEW (COMING SOON) -->
        <div id="course-track-sd-manager-view" class="space-y-6 hidden">
          <div class="glass-panel p-8 space-y-4 border border-cyberPurple/30 text-center">
            <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-cyberPurple/10 text-cyberPurple border border-cyberPurple/30 uppercase">Track 3: Coming Soon</span>
            <h3 class="text-2xl font-bold text-white">IT Service Desk Manager Leadership Track</h3>
            <p class="text-slate-300 text-xs max-w-xl mx-auto leading-relaxed">
              Curriculum in active production: Service Delivery Leadership, Shift-Left Strategy, CSAT/XLA Governance, Operational Budgeting, and Team KPI Dashboards.
            </p>
            <div class="pt-4">
              <button onclick="alert('Pre-registration recorded! We will notify you when Leadership Track goes live.')" class="cyber-btn bg-gradient-to-r from-cyberPurple to-cyberCyan"><i class="fa-solid fa-bell"></i> Pre-Register for Leadership Track (Free)</button>
            </div>
          </div>
        </div>

        <!-- TRACK 4: KNOWLEDGE BASE MANAGEMENT PREVIEW (COMING SOON) -->
        <div id="course-track-kbm-view" class="space-y-6 hidden">
          <div class="glass-panel p-8 space-y-4 border border-emerald-400/30 text-center">
            <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-400/10 text-emerald-400 border border-emerald-400/30 uppercase">Track 4: Coming Soon</span>
            <h3 class="text-2xl font-bold text-white">Knowledge Base Management (KBM) & KCS Track</h3>
            <p class="text-slate-300 text-xs max-w-xl mx-auto leading-relaxed">
              Curriculum in active production: Knowledge-Centered Service (KCS) methodology, Self-Service Deflection Portals, and AI Knowledge Graph Indexing.
            </p>
            <div class="pt-4">
              <button onclick="alert('Pre-registration recorded! We will notify you when KBM Track goes live.')" class="cyber-btn bg-gradient-to-r from-emerald-500 to-cyberCyan"><i class="fa-solid fa-bell"></i> Pre-Register for KBM Track (Free)</button>
            </div>
          </div>
        </div>

      </section>"""

# Replace existing tab-course section with new multi-track section
html = re.sub(
    r'<section id="tab-course".*?</section>',
    multi_course_section,
    html,
    flags=re.DOTALL
)

# Add selectCourseTrack JavaScript handler to inline script
select_track_js = """
  function selectCourseTrack(trackId) {
    console.log("Selected course track:", trackId);
    const tracks = ['sd-ops', 'mim', 'sd-manager', 'kbm'];
    tracks.forEach(t => {
      const card = document.getElementById('track-card-' + t);
      const view = document.getElementById('course-track-' + t + '-view');
      if (card) {
        card.classList.remove('border-2', 'border-amber-400', 'bg-amber-500/10');
        card.classList.add('border-white/[0.08]');
      }
      if (view) view.classList.add('hidden');
    });

    const activeCard = document.getElementById('track-card-' + trackId);
    const activeView = document.getElementById('course-track-' + trackId + '-view');
    if (activeCard) {
      activeCard.classList.add('border-2', 'border-amber-400', 'bg-amber-500/10');
      activeCard.classList.remove('border-white/[0.08]');
    }
    if (activeView) activeView.classList.remove('hidden');
  }
"""

if "function selectCourseTrack(" not in html:
    html = html.replace('function filterCourseLevel(', f'{select_track_js}\n  function filterCourseLevel(')

index_path.write_text(html, encoding="utf-8")
print("[OK] Upgraded Courses tab to Multi-Track Architecture with 4 Specialized Folders!")
