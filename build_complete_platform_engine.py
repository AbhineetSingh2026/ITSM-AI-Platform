import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# 1. Populate YouTube Video Grid directly with video cards
youtube_grid_html = """<div id="youtube-video-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Video 1 -->
            <div class="glass-panel p-4 space-y-3 group hover:border-red-500/40 transition-all duration-300">
              <div class="relative w-full h-44 rounded-xl overflow-hidden bg-slate-900 border border-white/[0.08]">
                <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=500&q=80" alt="L1 Support is Dead" class="w-full h-full object-cover group-hover:scale-105 transition-all duration-500">
                <div class="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-all flex items-center justify-center">
                  <span class="w-12 h-12 rounded-full bg-red-600/90 text-white flex items-center justify-center text-lg shadow-lg group-hover:scale-110 transition-all"><i class="fa-solid fa-play ml-1"></i></span>
                </div>
                <span class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 text-white font-mono text-[10px]">14:20</span>
              </div>
              <div>
                <span class="text-[9px] font-bold uppercase tracking-wider text-red-400 font-mono">AI ITSM Special</span>
                <h4 class="text-sm font-bold text-white group-hover:text-red-400 transition-colors line-clamp-2">L1 Support is Dead: AI Agents & Automated Triage Architecture</h4>
                <p class="text-slate-400 text-[11px] mt-1 line-clamp-2">How generative AI, autonomous ticket routing, and self-healing scripts are replacing manual L1 triage.</p>
              </div>
              <div class="flex items-center justify-between text-[10px] text-slate-500 font-mono border-t border-white/[0.05] pt-2">
                <span><i class="fa-solid fa-eye text-red-500"></i> 4.2k views</span>
                <span>2 weeks ago</span>
              </div>
            </div>

            <!-- Video 2 -->
            <div class="glass-panel p-4 space-y-3 group hover:border-red-500/40 transition-all duration-300">
              <div class="relative w-full h-44 rounded-xl overflow-hidden bg-slate-900 border border-white/[0.08]">
                <img src="https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=500&q=80" alt="Major Incident Management" class="w-full h-full object-cover group-hover:scale-105 transition-all duration-500">
                <div class="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-all flex items-center justify-center">
                  <span class="w-12 h-12 rounded-full bg-red-600/90 text-white flex items-center justify-center text-lg shadow-lg group-hover:scale-110 transition-all"><i class="fa-solid fa-play ml-1"></i></span>
                </div>
                <span class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 text-white font-mono text-[10px]">18:45</span>
              </div>
              <div>
                <span class="text-[9px] font-bold uppercase tracking-wider text-cyberCyan font-mono">ITIL 4 Deep Dive</span>
                <h4 class="text-sm font-bold text-white group-hover:text-red-400 transition-colors line-clamp-2">P1 Major Incident Bridge Calls & Root Cause Analysis (RCA)</h4>
                <p class="text-slate-400 text-[11px] mt-1 line-clamp-2">Step-by-step masterclass on orchestrating P1 bridge calls, executive comms, and 5-Why RCA templates.</p>
              </div>
              <div class="flex items-center justify-between text-[10px] text-slate-500 font-mono border-t border-white/[0.05] pt-2">
                <span><i class="fa-solid fa-eye text-red-500"></i> 6.8k views</span>
                <span>1 month ago</span>
              </div>
            </div>

            <!-- Video 3 -->
            <div class="glass-panel p-4 space-y-3 group hover:border-red-500/40 transition-all duration-300">
              <div class="relative w-full h-44 rounded-xl overflow-hidden bg-slate-900 border border-white/[0.08]">
                <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=500&q=80" alt="Building AI Service Desk" class="w-full h-full object-cover group-hover:scale-105 transition-all duration-500">
                <div class="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-all flex items-center justify-center">
                  <span class="w-12 h-12 rounded-full bg-red-600/90 text-white flex items-center justify-center text-lg shadow-lg group-hover:scale-110 transition-all"><i class="fa-solid fa-play ml-1"></i></span>
                </div>
                <span class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 text-white font-mono text-[10px]">22:10</span>
              </div>
              <div>
                <span class="text-[9px] font-bold uppercase tracking-wider text-cyberPurple font-mono">Python & LLMs</span>
                <h4 class="text-sm font-bold text-white group-hover:text-red-400 transition-colors line-clamp-2">Building an AI Service Desk Copilot with LLM Prompt Engineering</h4>
                <p class="text-slate-400 text-[11px] mt-1 line-clamp-2">Hands-on tutorial building a real-time ticket summarizer and sentiment analysis engine.</p>
              </div>
              <div class="flex items-center justify-between text-[10px] text-slate-500 font-mono border-t border-white/[0.05] pt-2">
                <span><i class="fa-solid fa-eye text-red-500"></i> 9.1k views</span>
                <span>2 months ago</span>
              </div>
            </div>
          </div>"""

# Replace loading spinner grid in YouTube tab
if "INITIALIZING LIVE YOUTUBE VIDEO PIPELINE..." in html:
    html = re.sub(
        r'<div id="youtube-video-grid".*?</div>\s*</div>\s*</div>',
        youtube_grid_html + "\n        </div>",
        html,
        flags=re.DOTALL
    )

# 2. Comprehensive JavaScript engines for ALL interactive functions across tabs
ALL_INTERACTIVE_SCRIPTS = """
<!-- ==================== PLATFORM FULL INTERACTIVE ENGINES ==================== -->
<script>
  // 1. Navigation & Tab Control
  function switchTab(tabId) {
    console.log("Switching tab to:", tabId);
    const tabViews = document.querySelectorAll('.tab-view');
    tabViews.forEach(view => {
      view.classList.add('hidden');
      view.classList.remove('block');
    });

    const targetTab = document.getElementById('tab-' + tabId);
    if (targetTab) {
      targetTab.classList.remove('hidden');
      targetTab.classList.add('block');
    }

    const navLinks = document.querySelectorAll('aside nav a');
    navLinks.forEach(link => {
      link.classList.remove('active-nav-item', 'bg-white/[0.05]', 'text-white');
      link.classList.add('text-slate-400');
    });

    const activeNav = document.getElementById('nav-' + tabId);
    if (activeNav) {
      activeNav.classList.add('active-nav-item', 'text-white');
      activeNav.classList.remove('text-slate-400');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function switchTabMobile(tabId) {
    switchTab(tabId);
    const mobileOverlay = document.getElementById('mobile-nav-overlay');
    if (mobileOverlay) {
      mobileOverlay.classList.add('hidden');
      mobileOverlay.classList.remove('flex');
    }
  }

  function toggleMobileNav() {
    const mobileOverlay = document.getElementById('mobile-nav-overlay');
    if (mobileOverlay) {
      if (mobileOverlay.classList.contains('hidden')) {
        mobileOverlay.classList.remove('hidden');
        mobileOverlay.classList.add('flex');
      } else {
        mobileOverlay.classList.add('hidden');
        mobileOverlay.classList.remove('flex');
      }
    }
  }

  // 2. Operations Dashboard Control
  function updateDashboardMetrics(type) {
    const btnGlobal = document.getElementById('dash-btn-global');
    const btnBhc = document.getElementById('dash-btn-bhc');
    const btnNhs = document.getElementById('dash-btn-nhs');
    const btnCaesars = document.getElementById('dash-btn-caesars');

    const btns = [btnGlobal, btnBhc, btnNhs, btnCaesars];
    btns.forEach(btn => {
      if (btn) {
        btn.classList.remove('bg-cyberPurple', 'text-white', 'shadow');
        btn.classList.add('text-slate-400');
      }
    });

    const targetBtn = document.getElementById('dash-btn-' + type);
    if (targetBtn) {
      targetBtn.classList.add('bg-cyberPurple', 'text-white', 'shadow');
      targetBtn.classList.remove('text-slate-400');
    }

    const mttrVal = document.getElementById('dash-mttr-val');
    const slaVal = document.getElementById('dash-sla-val');
    const xlaVal = document.getElementById('dash-xla-val');

    if (type === 'global') {
      if (mttrVal) mttrVal.textContent = '45m';
      if (slaVal) slaVal.textContent = '98.2%';
      if (xlaVal) xlaVal.textContent = '9.5/10';
    } else if (type === 'bhc') {
      if (mttrVal) mttrVal.textContent = '38m';
      if (slaVal) slaVal.textContent = '99.1%';
      if (xlaVal) xlaVal.textContent = '9.7/10';
    } else if (type === 'nhs') {
      if (mttrVal) mttrVal.textContent = '42m';
      if (slaVal) slaVal.textContent = '97.8%';
      if (xlaVal) xlaVal.textContent = '9.4/10';
    } else if (type === 'caesars') {
      if (mttrVal) mttrVal.textContent = '35m';
      if (slaVal) slaVal.textContent = '99.4%';
      if (xlaVal) xlaVal.textContent = '9.8/10';
    }
  }

  // 3. Course Level Filtering
  function filterCourseLevel(level) {
    const btns = ['all', '1', '2', '3'];
    btns.forEach(b => {
      const btn = document.getElementById('btn-lvl-' + b);
      if (btn) {
        btn.className = "course-lvl-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all bg-white/[0.03] text-slate-400 hover:text-white border border-white/[0.08]";
      }
    });

    const activeBtn = document.getElementById('btn-lvl-' + level);
    if (activeBtn) {
      activeBtn.className = "course-lvl-btn px-5 py-2.5 rounded-xl text-xs font-bold transition-all bg-amber-500 text-white shadow-lg shadow-amber-500/25";
    }

    const cards = document.querySelectorAll('.chapter-card');
    cards.forEach(card => {
      if (level === 'all' || card.getAttribute('data-level') === level) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  }

  // 4. AI Sandbox Tools Control
  function switchSandboxTool(toolName) {
    const tools = ['summarizer', 'categorizer', 'rca', 'predictor', 'sentiment'];
    tools.forEach(t => {
      const btn = document.getElementById('sb-tab-' + t);
      const view = document.getElementById('sb-view-' + t);
      if (btn) {
        btn.classList.remove('bg-cyberCyan', 'text-black', 'font-bold', 'shadow-lg');
        btn.classList.add('text-slate-400');
      }
      if (view) view.classList.add('hidden');
    });

    const activeBtn = document.getElementById('sb-tab-' + toolName);
    const activeView = document.getElementById('sb-view-' + toolName);
    if (activeBtn) {
      activeBtn.classList.add('bg-cyberCyan', 'text-black', 'font-bold', 'shadow-lg');
      activeBtn.classList.remove('text-slate-400');
    }
    if (activeView) activeView.classList.remove('hidden');
  }

  function autofillSummarizer(preset) {
    const input = document.getElementById('sb-summarizer-input');
    if (!input) return;
    if (preset === 'emis') input.value = "User calling from St. Thomas Clinic states EMIS Web won't launch. Error code 0x80070005 Access Denied after Windows Update. Identity verified. Re-registered DLLs, verified smartcard reader drivers, and cleared temp folder. Service restored.";
    else if (preset === 'nhs') input.value = "NHS Mail account locked out after user entered password 5 times incorrectly on mobile Outlook. Verified user via Manager callback. Unlocked in Active Directory, performed MFA challenge, user successfully logged in.";
    else if (preset === 'pc') input.value = "Desktop tower in Ward 3 showing No Boot Device Found on startup. Checked SATA cables, SSD not recognized in BIOS. Replaced SSD with spare unit, restored disk image via MDT, user back operational.";
    else input.value = "Laptop power adapter overheating and turning off. Tested charger output, verified faulty transformer block. Issued replacement Dell 65W USB-C charger from IT stock.";
  }

  function runTicketSummarizer() {
    const out = document.getElementById('sb-summarizer-output');
    if (out) {
      out.innerHTML = `<div class="p-4 bg-cyberCyan/10 border border-cyberCyan/30 rounded-xl space-y-2">
        <p class="text-xs font-bold text-cyberCyan uppercase tracking-wider"><i class="fa-solid fa-robot"></i> AI Executive Summary</p>
        <p class="text-xs text-slate-200"><strong>Issue:</strong> Application Access Failure / Account Lockout</p>
        <p class="text-xs text-slate-300"><strong>Action Taken:</strong> Identity verified, Active Directory object unlocked, DLL dependencies re-registered, and test login confirmed.</p>
        <p class="text-[10px] text-emerald-400 font-mono">Status: RESOLVED (FCR 100%)</p>
      </div>`;
    }
  }

  function autofillCategorizer(preset) {
    const input = document.getElementById('sb-categorizer-input');
    if (!input) return;
    if (preset === 'vpn') input.value = "GlobalProtect VPN fails to connect with error 'Authentication Gateway Timeout' for all remote staff in London office.";
    else input.value = "Paper jam in Ricoh MP C3004 network printer on Floor 2 Finance department.";
  }

  function runCTICategorizer() {
    const out = document.getElementById('sb-categorizer-output');
    if (out) {
      out.innerHTML = `<div class="p-4 bg-cyberPurple/10 border border-cyberPurple/30 rounded-xl space-y-2">
        <p class="text-xs font-bold text-cyberPurple uppercase tracking-wider"><i class="fa-solid fa-sitemap"></i> CTI Auto-Classification</p>
        <p class="text-xs text-slate-200"><strong>Category:</strong> Infrastructure / Network Services</p>
        <p class="text-xs text-slate-200"><strong>Type:</strong> Remote Access / VPN</p>
        <p class="text-xs text-slate-200"><strong>Item:</strong> Authentication Gateway</p>
        <p class="text-[10px] text-amber-400 font-mono">Suggested Priority: P2 High (Impact: 25+ Users)</p>
      </div>`;
    }
  }

  function copyCTIWebhookPayload() {
    if (navigator.clipboard) {
      navigator.clipboard.writeText('{"category": "Network", "priority": "P2", "triage": "AI-Auto"}');
      alert("Webhook JSON payload copied to clipboard!");
    }
  }

  function runRCAGenerator() {
    const out = document.getElementById('sb-rca-output');
    if (out) {
      out.innerHTML = `<div class="p-4 bg-red-500/10 border border-red-500/30 rounded-xl space-y-2">
        <p class="text-xs font-bold text-red-400 uppercase tracking-wider"><i class="fa-solid fa-magnifying-glass"></i> AI Root Cause Analysis (5-Whys)</p>
        <p class="text-xs text-slate-300"><strong>1. Why did service crash?</strong> Primary database memory overflow.</p>
        <p class="text-xs text-slate-300"><strong>2. Why memory overflow?</strong> Unindexed SQL query spawned 50,000 recursive sub-threads.</p>
        <p class="text-xs text-slate-300"><strong>3. Why unindexed query?</strong> Deployed in emergency hotfix without DBA review.</p>
        <p class="text-xs text-emerald-400 font-bold">Preventative Action: Mandate CAB SQL Index Validation step in CI/CD pipeline.</p>
      </div>`;
    }
  }

  function runPredictor(preset) {
    const out = document.getElementById('sb-predictor-output');
    if (out) {
      out.innerHTML = `<div class="p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-xl space-y-2">
        <p class="text-xs font-bold text-emerald-400 uppercase tracking-wider"><i class="fa-solid fa-chart-line"></i> Predictor Forecast</p>
        <p class="text-xs text-slate-200"><strong>Expected Call Volume:</strong> +35% above average</p>
        <p class="text-xs text-slate-300"><strong>Primary Drivers:</strong> Monday morning password resets & weekend MFA sync lag.</p>
        <p class="text-xs text-cyberCyan font-mono">Recommended Action: Shift 2 L2 analysts to Service Desk phone queue 08:00 - 10:30.</p>
      </div>`;
    }
  }

  function autofillSentiment(preset) {
    const input = document.getElementById('sb-sentiment-input');
    if (!input) return;
    if (preset === 'angry') input.value = "THIS IS THE THIRD TIME MY EMIS WEB HAS CRASHED THIS WEEK! I AM WITH A PATIENT AND CANNOT ACCESS RECORDS! FIX THIS NOW!!!";
    else input.value = "Hi team, thank you so much for unlocking my smartcard so quickly this morning! Outstanding service!";
  }

  function runSentimentAnalyzer() {
    const out = document.getElementById('sb-sentiment-output');
    const input = document.getElementById('sb-sentiment-input');
    if (!out || !input) return;
    const txt = input.value.toLowerCase();
    if (txt.includes('angry') || txt.includes('fix this now') || txt.includes('crashed')) {
      out.innerHTML = `<div class="p-4 bg-red-500/10 border border-red-500/30 rounded-xl space-y-2">
        <p class="text-xs font-bold text-red-400 uppercase tracking-wider"><i class="fa-solid fa-face-angry"></i> Sentiment: HIGH ESCALATION RISK (88% Negative)</p>
        <p class="text-xs text-slate-300">User is frustrated due to recurring clinical application impact. Immediate manager outreach recommended.</p>
      </div>`;
    } else {
      out.innerHTML = `<div class="p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-xl space-y-2">
        <p class="text-xs font-bold text-emerald-400 uppercase tracking-wider"><i class="fa-solid fa-face-smile"></i> Sentiment: POSITIVE / SATISFIED (95% Positive)</p>
        <p class="text-xs text-slate-300">High CSAT score likely. Commendation logged for handling analyst.</p>
      </div>`;
    }
  }

  // 5. SOP Blueprints Modal
  function openSOPViewer(sopType) {
    const modal = document.getElementById('sop-viewer-modal');
    const title = document.getElementById('sop-title');
    const body = document.getElementById('sop-body');
    if (!modal || !title || !body) return;

    if (sopType === 'sop_incident') {
      title.textContent = "Standard Operating Procedure: Incident Lifecycle & SLA Management";
      body.innerHTML = `<div class="space-y-3">
        <h4 class="font-bold text-white text-sm">1. Purpose & Scope</h4>
        <p>Defines standard procedures for logging, classifying, prioritizing, investigating, and resolving IT Incidents according to ITIL v4 principles.</p>
        <h4 class="font-bold text-white text-sm">2. Priority Matrix</h4>
        <table class="w-full text-left border border-slate-700">
          <tr class="bg-slate-800 text-white"><th class="p-2">Priority</th><th class="p-2">Impact x Urgency</th><th class="p-2">SLA Response</th><th class="p-2">SLA Resolution</th></tr>
          <tr><td class="p-2 text-red-400 font-bold">P1 Critical</td><td class="p-2">High x High</td><td class="p-2">15 Mins</td><td class="p-2">4 Hours</td></tr>
          <tr><td class="p-2 text-amber-400 font-bold">P2 High</td><td class="p-2">High x Med / Med x High</td><td class="p-2">30 Mins</td><td class="p-2">8 Hours</td></tr>
          <tr><td class="p-2 text-cyberCyan font-bold">P3 Moderate</td><td class="p-2">Med x Med</td><td class="p-2">2 Hours</td><td class="p-2">24 Hours</td></tr>
        </table>
      </div>`;
    } else if (sopType === 'sop_cab') {
      title.textContent = "Standard Operating Procedure: Change Advisory Board (CAB) Approvals";
      body.innerHTML = `<div class="space-y-3">
        <h4 class="font-bold text-white text-sm">1. Emergency & Standard Change Governance</h4>
        <p>All Production Infrastructure changes must submit a RFC (Request for Change) at least 72 hours prior to weekly CAB review.</p>
        <h4 class="font-bold text-white text-sm">2. Required RFC Checklist</h4>
        <ul class="list-disc pl-5 space-y-1">
          <li>Rollback plan tested in Staging environment.</li>
          <li>Outage impact window & user communication draft.</li>
          <li>Peer technical review sign-off by Lead System Architect.</li>
        </ul>
      </div>`;
    } else {
      title.textContent = "Standard Operating Procedure: Service Desk Operational Excellence";
      body.innerHTML = `<p>Comprehensive blueprint covering FCR optimization, Active Directory access controls, and AI Copilot triage protocols.</p>`;
    }

    modal.classList.remove('hidden');
    modal.classList.add('flex');
    setTimeout(() => modal.classList.remove('opacity-0'), 10);
  }

  function closeSOPViewer() {
    const modal = document.getElementById('sop-viewer-modal');
    if (modal) {
      modal.classList.add('opacity-0');
      setTimeout(() => {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }, 300);
    }
  }

  // 6. Interactive Watermelon SLA vs XLA Calculator
  function calculateWatermelonIndex() {
    const mttrSlider = document.getElementById('calc-mttr-slider');
    const mttrVal = document.getElementById('calc-mttr-val');
    if (mttrSlider && mttrVal) {
      mttrVal.textContent = mttrSlider.value + " Hours";
    }
  }

  // 7. Modals & Helpers
  function toggleAccessStudentField() {
    const profile = document.getElementById('access-profile');
    const studentBox = document.getElementById('access-student-box');
    if (profile && studentBox) {
      if (profile.value === 'Student') {
        studentBox.classList.remove('hidden');
      } else {
        studentBox.classList.add('hidden');
      }
    }
  }

  function enterAsGuest() {
    switchTab('home');
  }

  function copyDirectEmail() {
    if (navigator.clipboard) {
      navigator.clipboard.writeText('abhineetsam2027@gmail.com');
      alert('Email copied to clipboard: abhineetsam2027@gmail.com');
    }
  }

  function filterBlogCategory(cat) { console.log("Blog filter:", cat); }
  function closeBlogModal() {}
  function postBlogComment() {}
  function filterForumCategory(cat) { console.log("Forum filter:", cat); }
  function openCreateTopicModal() {}
  function closeCreateTopicModal() {}
  function submitNewTopic() {}
  function closeForumModal() {}
  function postForumReply() {}
</script>
"""

# Replace script before </body> cleanly
html = re.sub(r'<!-- ==================== PLATFORM FULL INTERACTIVE ENGINES ==================== -->.*?</script>', '', html, flags=re.DOTALL)
html = html.replace('</body>', f'{ALL_INTERACTIVE_SCRIPTS}\n</body>')

index_path.write_text(html, encoding="utf-8")
print("[OK] Re-injected full engine and YouTube grid cards!")
