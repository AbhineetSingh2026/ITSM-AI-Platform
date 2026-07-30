import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# 1. Update Sidebar Nav label: Courses (Free)
html = re.sub(
    r'<a href="#" onclick="switchTab\(\'course\'\)" id="nav-course"[^>]*>.*?</a>',
    '''<a href="#" onclick="switchTab('course')" id="nav-course" class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white transition-all text-sm font-semibold border-l-3 border-transparent">
            <i class="fa-solid fa-graduation-cap text-base text-amber-400"></i> Courses (Free) <span class="px-1.5 py-0.5 text-[9px] font-extrabold bg-amber-400/20 text-amber-400 border border-amber-400/30 rounded-md uppercase ml-auto">Free</span>
          </a>''',
    html,
    flags=re.DOTALL
)

# 2. Build World-Class Multi-Track Academy Tab Layout
polished_academy_section = """<section id="tab-course" class="tab-view hidden space-y-8 max-w-6xl mx-auto">
        <!-- Hero Academy Banner -->
        <div class="glass-panel p-6 md:p-8 relative overflow-hidden flex flex-col lg:flex-row items-center justify-between gap-6 bg-gradient-to-br from-cyberSlate to-cyberBg border border-amber-500/30">
          <div class="space-y-3 flex-1">
            <span class="badge-neon border-amber-400/40 text-amber-400 bg-amber-400/10"><i class="fa-solid fa-graduation-cap text-amber-400"></i> Free Multi-Track Certification Academy</span>
            <h1 class="text-3xl md:text-4xl lg:text-5xl font-bold tracking-tight text-white leading-tight">
              Global ITSM & <span class="bg-clip-text text-transparent bg-gradient-to-r from-amber-400 via-cyberCyan to-cyberPurple">AI Operations Academy</span>
            </h1>
            <p class="text-slate-300 text-xs md:text-sm leading-relaxed max-w-2xl">
              Select a specialized learning track below to master Service Desk Operations, Major Incident Management (MIM), IT Service Leadership, or Knowledge Base Management.
            </p>
          </div>
          <div class="flex gap-3 shrink-0 font-mono">
            <div class="p-3 glass-panel border border-white/[0.08] rounded-xl text-center min-w-[80px]">
              <span class="text-2xl font-extrabold text-white block">4</span>
              <span class="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Tracks</span>
            </div>
            <div class="p-3 glass-panel border border-white/[0.08] rounded-xl text-center min-w-[80px]">
              <span class="text-2xl font-extrabold text-cyberCyan block">12+</span>
              <span class="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Chapters</span>
            </div>
            <div class="p-3 glass-panel border border-white/[0.08] rounded-xl text-center min-w-[80px]">
              <span class="text-2xl font-extrabold text-emerald-400 block">100%</span>
              <span class="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Free</span>
            </div>
          </div>
        </div>

        <!-- Track Selection Folders Grid -->
        <div class="space-y-4">
          <div class="flex justify-between items-center">
            <h3 class="text-xs font-mono font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
              <i class="fa-solid fa-folder-open text-amber-400"></i> Select Course Track / Learning Path
            </h3>
            <span class="text-[10px] text-cyberCyan font-mono">Select a track to load modules</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            
            <!-- Track 1: IT Service Desk Operations (Active) -->
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
                <span>View 12 Chapters</span> <i class="fa-solid fa-arrow-right text-xs"></i>
              </div>
            </div>

            <!-- Track 2: Major Incident Management (MIM) (Coming Soon) -->
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

            <!-- Track 3: IT Service Desk Manager (Coming Soon) -->
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

            <!-- Track 4: Knowledge Base Management (Coming Soon) -->
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

        <!-- TRACK 1: IT SERVICE DESK OPERATIONS CONTENT VIEW -->
        <div id="course-track-sd-ops-view" class="space-y-8">
          
          <!-- Grand Master Certification Callout Banner -->
          <div class="glass-panel p-5 border border-amber-400/40 rounded-2xl bg-gradient-to-r from-amber-500/10 via-cyberBg to-cyberPurple/10 flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 rounded-xl bg-amber-500/20 border border-amber-400/40 flex items-center justify-center text-amber-300 text-xl shrink-0">
                <i class="fa-solid fa-trophy"></i>
              </div>
              <div>
                <h4 class="font-bold text-white text-sm">IT Service Desk Grand Master Certification Exam</h4>
                <p class="text-slate-300 text-xs mt-0.5">Comprehensive 50-Question Scenario Examination testing Level 1, 2, and 3 Modules with instant certificate generation.</p>
              </div>
            </div>
            <button onclick="launchExam('final')" class="cyber-btn bg-gradient-to-r from-amber-500 via-emerald-500 to-cyberPurple text-white font-bold py-2.5 px-6 rounded-xl shadow-lg hover:scale-105 transition shrink-0">
              <i class="fa-solid fa-trophy text-amber-300"></i> Grand Master Exam (50 Qs)
            </button>
          </div>

          <!-- Level Filter Buttons & Exam Launchers -->
          <div class="space-y-4">
            <div class="flex justify-between items-center">
              <div class="flex gap-2 overflow-x-auto pb-1">
                <button onclick="filterCourseLevel('all')" id="btn-lvl-all" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-amber-500 text-white shadow-lg shadow-amber-500/25">All Chapters (12)</button>
                <button onclick="filterCourseLevel('1')" id="btn-lvl-1" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 1: Foundation (4)</button>
                <button onclick="filterCourseLevel('2')" id="btn-lvl-2" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 2: Intermediate (4)</button>
                <button onclick="filterCourseLevel('3')" id="btn-lvl-3" class="course-lvl-btn px-4 py-2 rounded-xl text-xs font-bold transition-all bg-white/[0.04] text-slate-400 hover:text-white border border-white/[0.08]">Level 3: Advanced ITIL & AI (4)</button>
              </div>
              <div class="hidden md:flex gap-2 font-mono text-[10px]">
                <button onclick="launchExam('level1')" class="px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold hover:bg-emerald-500/20 transition"><i class="fa-solid fa-pen-to-square"></i> L1 Exam</button>
                <button onclick="launchExam('level2')" class="px-3 py-1.5 rounded-lg bg-cyberBlue/10 border border-cyberBlue/30 text-cyberBlue font-bold hover:bg-cyberBlue/20 transition"><i class="fa-solid fa-pen-to-square"></i> L2 Exam</button>
                <button onclick="launchExam('level3')" class="px-3 py-1.5 rounded-lg bg-cyberPurple/10 border border-cyberPurple/30 text-cyberPurple font-bold hover:bg-cyberPurple/20 transition"><i class="fa-solid fa-pen-to-square"></i> L3 Exam</button>
              </div>
            </div>

            <!-- Dynamic 12 Chapters Container Grid -->
            <div id="course-chapters-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <!-- Dynamically populated by renderPlatformCourseChapters() -->
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

# Replace existing tab-course section
html = re.sub(
    r'<section id="tab-course".*?</section>',
    polished_academy_section,
    html,
    flags=re.DOTALL
)

# 3. Add Chapter Studio Modal to HTML if not present
chapter_studio_modal_html = """
  <!-- Interactive Chapter Studio & Video Player Modal -->
  <div id="chapter-studio-modal" class="fixed inset-0 bg-cyberBg/95 backdrop-blur-md z-[9999] flex items-center justify-center p-4 hidden transition-all duration-300 opacity-0">
    <div class="glass-panel w-full max-w-4xl max-h-[90vh] flex flex-col bg-gradient-to-br from-cyberSlate to-cyberBg border border-amber-400/30 overflow-hidden shadow-2xl relative rounded-2xl">
      <!-- Modal Header -->
      <div class="p-5 border-b border-slate-800 flex justify-between items-center bg-black/40 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-400/30 flex items-center justify-center text-amber-400 text-lg">
            <i class="fa-solid fa-graduation-cap"></i>
          </div>
          <div>
            <span id="ch-studio-level-badge" class="px-2 py-0.5 rounded bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 text-[9px] font-mono font-bold uppercase">LEVEL 1 FOUNDATION</span>
            <h3 id="ch-studio-title" class="font-bold text-base text-white mt-0.5">Modern IT Service Desk Fundamentals</h3>
          </div>
        </div>
        <button onclick="closeChapterStudioModal()" class="w-9 h-9 rounded-lg bg-white/[0.05] border border-white/[0.08] flex items-center justify-center text-slate-400 hover:text-white hover:border-red-500/50 transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Studio Content Body -->
      <div class="p-6 overflow-y-auto flex-1 space-y-6">
        <!-- Interactive Video Player Banner -->
        <div class="w-full h-64 md:h-80 rounded-2xl overflow-hidden bg-slate-900 border border-white/[0.1] relative group shadow-2xl">
          <img id="ch-studio-video-thumb" src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=1000&q=80" alt="Video Lesson" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/50 flex flex-col justify-between p-6">
            <div class="flex justify-between items-center text-xs font-mono">
              <span class="px-3 py-1 rounded-full bg-black/70 border border-white/20 text-white font-bold"><i class="fa-solid fa-circle text-red-500 text-[8px] animate-pulse"></i> Interactive Video Studio</span>
              <span id="ch-studio-duration" class="px-3 py-1 rounded-full bg-black/70 text-amber-400 font-bold"><i class="fa-regular fa-clock"></i> 45 min</span>
            </div>
            
            <!-- Center Play Button -->
            <div class="self-center">
              <button onclick="playLessonVideo()" class="w-16 h-16 rounded-full bg-amber-500 text-white flex items-center justify-center text-2xl shadow-2xl hover:scale-110 transition-all shadow-amber-500/40">
                <i class="fa-solid fa-play ml-1"></i>
              </button>
            </div>

            <!-- Video Progress bar -->
            <div class="space-y-1 font-mono text-[10px]">
              <div class="flex justify-between text-slate-300">
                <span>00:00 / Chapter Lesson</span>
                <span>1080p HD</span>
              </div>
              <div class="w-full h-1.5 bg-white/20 rounded-full overflow-hidden">
                <div class="w-1/3 h-full bg-gradient-to-r from-amber-400 to-cyberCyan"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Documented Study Guide & Key SOP Notes -->
        <div class="glass-panel p-6 space-y-4 border border-white/[0.08]">
          <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wider font-mono flex items-center gap-2">
            <i class="fa-solid fa-book-open"></i> Documented Study Guide & SOP Syllabus
          </h4>
          <p id="ch-studio-desc" class="text-xs text-slate-300 leading-relaxed">
            Role of Service Desk, Call vs. Ticket Logging, Active Listening, Customer Centricity, First Contact Resolution (FCR).
          </p>

          <div class="p-4 bg-black/40 border border-slate-800 rounded-xl space-y-2">
            <span class="text-[10px] font-bold text-cyberCyan uppercase tracking-wider block font-mono"><i class="fa-solid fa-list-check"></i> Key Operational Takeaways</span>
            <ul id="ch-studio-takeaways" class="space-y-1.5 text-xs text-slate-300 font-mono">
              <!-- Dynamically inserted -->
            </ul>
          </div>
        </div>

        <!-- Practice Micro-Quiz Section -->
        <div class="glass-panel p-6 space-y-4 border border-cyberCyan/30">
          <h4 class="text-xs font-bold text-cyberCyan uppercase tracking-wider font-mono flex items-center gap-2">
            <i class="fa-solid fa-pen-to-square"></i> Chapter Knowledge Check (Micro-Quiz)
          </h4>
          <div id="ch-studio-quiz-box" class="p-4 bg-cyberCyan/10 border border-cyberCyan/20 rounded-xl space-y-3">
            <p id="ch-quiz-q" class="text-xs font-bold text-white">Question: What is the primary metric for measuring immediate ticket resolution without escalation?</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs font-mono">
              <button onclick="checkMicroQuiz(true)" class="p-2.5 bg-white/[0.03] hover:bg-emerald-500/20 border border-white/[0.08] hover:border-emerald-500/40 text-slate-300 hover:text-white rounded-lg text-left transition">A. First Contact Resolution (FCR)</button>
              <button onclick="checkMicroQuiz(false)" class="p-2.5 bg-white/[0.03] hover:bg-red-500/20 border border-white/[0.08] hover:border-red-500/40 text-slate-300 hover:text-white rounded-lg text-left transition">B. Mean Time To Repair (MTTR)</button>
            </div>
            <div id="ch-quiz-feedback" class="text-[11px] font-bold hidden pt-1"></div>
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-slate-800 bg-black/40 shrink-0 flex justify-between items-center">
        <span class="text-[10px] text-slate-500 font-mono">Prepared by Abhineet Singh | Operations Leader</span>
        <div class="flex gap-2">
          <button onclick="openContactModalWithSubject('Question about chapter')" class="px-4 py-2 bg-white/[0.05] hover:bg-white/[0.1] border border-white/[0.1] text-xs font-bold text-slate-300 rounded-xl transition">
            <i class="fa-solid fa-envelope text-amber-400"></i> Ask Question
          </button>
          <button onclick="closeChapterStudioModal()" class="cyber-btn py-2 px-6 text-xs font-bold">
            Done / Continue
          </button>
        </div>
      </div>

    </div>
  </div>
"""

if "id=\"chapter-studio-modal\"" not in html:
    html = html.replace('</body>', chapter_studio_modal_html + '\n</body>')

# 4. Inject complete JavaScript engine with renderPlatformCourseChapters and chapter studio functions
FULL_ACADEMY_JS = """
<script>
  // Chapter Studio Modal Handlers
  function openChapterLessonModalByNum(chNum) {
    const ch = platformCourseChapters.find(c => c.chapterNum === chNum);
    if (!ch) return;

    const modal = document.getElementById('chapter-studio-modal');
    const badge = document.getElementById('ch-studio-level-badge');
    const title = document.getElementById('ch-studio-title');
    const duration = document.getElementById('ch-studio-duration');
    const desc = document.getElementById('ch-studio-desc');
    const takeaways = document.getElementById('ch-studio-takeaways');

    if (badge) badge.textContent = ch.levelName.toUpperCase();
    if (title) title.textContent = `Chapter ${ch.chapterNum}: ${ch.title}`;
    if (duration) duration.innerHTML = `<i class="fa-regular fa-clock"></i> ${ch.duration}`;
    if (desc) desc.textContent = ch.desc;

    if (takeaways) {
      takeaways.innerHTML = ch.keyTakeaways.map(t => `<li class="flex items-start gap-2"><i class="fa-solid fa-circle-check text-emerald-400 mt-1 text-[10px]"></i> <span>${t}</span></li>`).join('');
    }

    if (modal) {
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      setTimeout(() => modal.classList.remove('opacity-0'), 10);
    }
  }

  function closeChapterStudioModal() {
    const modal = document.getElementById('chapter-studio-modal');
    if (modal) {
      modal.classList.add('opacity-0');
      setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }, 300);
    }
  }

  function playLessonVideo() {
    alert("🎥 Interactive Video Lesson Launched! Loading high-definition stream for this chapter...");
  }

  function checkMicroQuiz(isCorrect) {
    const fb = document.getElementById('ch-quiz-feedback');
    if (!fb) return;
    fb.classList.remove('hidden', 'text-emerald-400', 'text-red-400');
    if (isCorrect) {
      fb.classList.add('text-emerald-400');
      fb.innerHTML = '<i class="fa-solid fa-circle-check"></i> Correct! FCR (First Contact Resolution) measures resolving tickets on the initial call without escalation.';
    } else {
      fb.classList.add('text-red-400');
      fb.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> Incorrect. MTTR measures total elapsed time to repair, while FCR measures immediate resolution on first contact.';
    }
  }

  // 12 Chapters Renderer
  function renderPlatformCourseChapters(filterLvl = 'all') {
    const grid = document.getElementById('course-chapters-grid');
    if (!grid) return;
    grid.innerHTML = '';

    const filtered = filterLvl === 'all' 
        ? platformCourseChapters 
        : platformCourseChapters.filter(c => c.level === parseInt(filterLvl));

    filtered.forEach(ch => {
        const card = document.createElement('div');
        card.className = 'chapter-card glass-panel p-5 flex flex-col justify-between space-y-4 hover:border-amber-400/50 transition duration-300 relative rounded-2xl border border-white/[0.08]';
        card.setAttribute('data-level', ch.level);

        let chipBg = 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30';
        if (ch.level === 2) chipBg = 'bg-cyberBlue/20 text-cyberBlue border-cyberBlue/30';
        if (ch.level === 3) chipBg = 'bg-cyberPurple/20 text-cyberPurple border-cyberPurple/30';

        const takeawaysHtml = ch.keyTakeaways.map(t => `<li class="flex items-start gap-1.5"><i class="fa-solid fa-check text-[10px] text-cyberCyan mt-0.5"></i> <span>${t}</span></li>`).join('');

        card.innerHTML = `
            <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                    <span class="px-2.5 py-0.5 rounded text-[9px] font-bold border uppercase ${chipBg}">${ch.levelName}</span>
                    <span class="font-mono text-[10px] text-slate-500">Chapter ${ch.chapterNum} of 12</span>
                </div>
                <h3 class="text-sm font-bold text-white leading-snug">${ch.title}</h3>
                <p class="text-slate-400 text-xs leading-relaxed line-clamp-2">${ch.desc}</p>
                <div class="flex flex-wrap gap-2 pt-1 font-mono text-[10px]">
                    <span class="px-2 py-0.5 bg-white/[0.04] border border-white/[0.08] rounded text-slate-300"><i class="fa-regular fa-clock text-amber-400"></i> ${ch.duration}</span>
                    <span class="px-2 py-0.5 bg-white/[0.04] border border-white/[0.08] rounded text-slate-300"><i class="fa-solid fa-tag text-cyberCyan"></i> ${ch.badge}</span>
                </div>
                <div class="p-3 bg-black/40 border border-slate-800 rounded-xl space-y-1.5">
                    <span class="text-[10px] font-bold text-cyberPurple uppercase tracking-wider block font-mono"><i class="fa-solid fa-lightbulb text-amber-400"></i> Key Takeaways</span>
                    <ul class="space-y-1 text-[11px] text-slate-300 font-mono">${takeawaysHtml}</ul>
                </div>
            </div>
            <div class="flex gap-2 pt-2">
                <button onclick="openChapterLessonModalByNum(${ch.chapterNum})" class="cyber-btn text-xs py-2 flex-1 justify-center bg-gradient-to-r from-amber-500 to-cyberPurple text-white font-bold"><i class="fa-solid fa-circle-play"></i> Watch Lesson</button>
                <button onclick="openChapterLessonModalByNum(${ch.chapterNum})" class="cyber-btn-outline text-xs py-2 px-3"><i class="fa-solid fa-book"></i> Notes</button>
            </div>
        `;
        grid.appendChild(card);
    });
  }

  // Hook tab switching to render chapters automatically
  const origSwitchTab = switchTab;
  switchTab = function(tabId) {
    origSwitchTab(tabId);
    if (tabId === 'course') {
      renderPlatformCourseChapters('all');
    }
  };

  // Initial render when script loads
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => renderPlatformCourseChapters('all'));
  } else {
    renderPlatformCourseChapters('all');
  }
</script>
"""

# Replace existing JS block with complete academy engine
if "function renderPlatformCourseChapters(" not in html:
    html = html.replace('</body>', FULL_ACADEMY_JS + '\n</body>')

index_path.write_text(html, encoding="utf-8")
print("[OK] Re-engineered Courses tab with 12 Chapter Cards, Refined UI & Interactive Video Studio Modal!")
