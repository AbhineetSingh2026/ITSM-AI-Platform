import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# 1. Update Head with Schema.org JSON-LD Structured Data & Clean SPA Routing Script
json_ld_schema = """
  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Person",
        "@id": "https://itsm-ai-platform.vercel.app/#person",
        "name": "Abhineet Singh",
        "jobTitle": "IT Operations Manager & ITSM Product Owner",
        "worksFor": {
          "@type": "Organization",
          "name": "AI-ITSM Hub"
        },
        "url": "https://itsm-ai-platform.vercel.app/",
        "sameAs": [
          "https://www.youtube.com/@AIDrivenITManager",
          "https://www.linkedin.com/in/abhineetsingh"
        ],
        "knowsAbout": ["IT Service Management", "ITIL 4", "AI Operations", "ServiceDesk Automation", "Halo ESM", "ServiceNow"]
      },
      {
        "@type": "Course",
        "@id": "https://itsm-ai-platform.vercel.app/#course-sd-ops",
        "name": "IT Service Desk Operations & AI Triage Masterclass",
        "description": "12-Chapter professional training program covering IT helpdesk basics, L1-L2 troubleshooting, Active Directory, SLAs, XLAs, and AI virtual agent automation.",
        "provider": {
          "@type": "Organization",
          "name": "AI-ITSM Hub",
          "url": "https://itsm-ai-platform.vercel.app/"
        },
        "hasCourseInstance": {
          "@type": "CourseInstance",
          "courseMode": "Online",
          "instructor": {
            "@id": "https://itsm-ai-platform.vercel.app/#person"
          }
        }
      }
    ]
  }
  </script>
"""

if 'type="application/ld+json"' not in html:
    html = html.replace('</head>', f'{json_ld_schema}\n</head>')

# 2. Standardize Experience Statement in Hero to 20+ Years
html = html.replace('17+ Years Experience', '20+ Years Experience')
html = html.replace('Over 20 years', '20+ years')

# 3. Update ITIL badge to "ITIL 4 Aligned Operating Model"
html = html.replace('ITIL Compliant', 'ITIL 4 Aligned Operating Model')

# 4. Add Metric Source Disclaimer to IT Operations Dashboard
metric_disclaimer = """
            <p class="text-[10px] text-slate-400 font-mono text-center pt-2">
              <i class="fa-solid fa-shield-halved text-cyberCyan"></i> <em>Illustrative Demo & Anonymized Benchmark Metrics — Based on multi-site enterprise IT Operations improvement programs.</em>
            </p>
"""
if 'Illustrative Demo & Anonymized Benchmark Metrics' not in html:
    html = html.replace('<!-- Statistics -->', f'{metric_disclaimer}\n<!-- Statistics -->')

# 5. Rename Grand Master Exam to "AI-ITSM Hub Certificate of Completion" & Add Disclaimer
html = html.replace(
    'IT Service Desk Grand Master Certification Exam',
    'AI-ITSM Hub Service Desk Skills Certificate Exam'
)
html = html.replace(
    'Comprehensive 50-Question Scenario Examination testing Level 1, 2, and 3 Modules with instant certificate generation.',
    'Comprehensive 50-Question Scenario Examination testing Level 1–3 Modules. <span class="block text-[10px] text-amber-300 mt-0.5"><em>Independent Professional Learning Certificate — Not affiliated with or endorsed by PeopleCert, Axelos, or ITIL.</em></span>'
)

# 6. Add Diagnostic Navigation Link to Sidebar
diag_nav_link = """
          <a href="#/diagnostic" onclick="switchTab('diagnostic')" id="nav-diagnostic" class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white transition-all text-sm font-semibold border-l-3 border-transparent">
            <i class="fa-solid fa-clipboard-check text-base text-cyberCyan"></i> Skills Diagnostic <span class="px-1.5 py-0.5 text-[9px] font-extrabold bg-cyberCyan/20 text-cyberCyan border border-cyberCyan/30 rounded-md uppercase ml-auto">25 Qs</span>
          </a>
          <a href="#/templates" onclick="switchTab('templates')" id="nav-templates" class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:text-white transition-all text-sm font-semibold border-l-3 border-transparent">
            <i class="fa-solid fa-file-signature text-base text-emerald-400"></i> SOP Templates
          </a>
"""

if 'id="nav-diagnostic"' not in html:
    html = html.replace('<a href="#" onclick="switchTab(\'course\')" id="nav-course"', f'{diag_nav_link}\n          <a href="#/course" onclick="switchTab(\'course\')" id="nav-course"')

# 7. Add AI Sandbox Warning Banner & Controls
sandbox_warning_banner = """
          <!-- Permanent AI Governance & Privacy Warning Banner -->
          <div class="p-4 bg-amber-500/10 border border-amber-400/40 rounded-2xl flex items-start gap-3 text-xs text-amber-300">
            <i class="fa-solid fa-triangle-exclamation text-amber-400 text-lg shrink-0 mt-0.5"></i>
            <div>
              <p class="font-bold uppercase tracking-wider text-[11px] font-mono">AI Sandbox Security & Privacy Governance Warning</p>
              <p class="text-slate-300 text-[11px] mt-0.5">Do NOT enter real passwords, patient data, personal PII, or confidential credentials. Use synthetic or anonymized examples only. All AI outputs serve as recommendations requiring human-in-the-loop review.</p>
            </div>
          </div>
"""

if 'AI Sandbox Security & Privacy Governance Warning' not in html:
    html = html.replace(
        '<p class="text-slate-300 text-xs">Test live AI algorithms for Ticket Summarization, Auto-Classification, 5-Why RCA, and Incident Volume Forecasting.</p>',
        f'<p class="text-slate-300 text-xs">Test live AI algorithms for Ticket Summarization, Auto-Classification, 5-Why RCA, and Incident Volume Forecasting.</p>\n{sandbox_warning_banner}'
    )

# 8. Add Diagnostic Tab View Section HTML (`#tab-diagnostic`)
diagnostic_tab_html = """
      <!-- ==================== SKILLS DIAGNOSTIC TAB ==================== -->
      <section id="tab-diagnostic" class="tab-view hidden space-y-8 max-w-6xl mx-auto">
        <div class="glass-panel p-8 space-y-6 rounded-3xl border border-cyberCyan/30">
          <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div class="space-y-2">
              <span class="px-3.5 py-1.5 rounded-full text-xs font-bold bg-cyberCyan/10 border border-cyberCyan/30 text-cyberCyan inline-flex items-center gap-2">
                <i class="fa-solid fa-clipboard-check"></i> Career Diagnostic Assessment
              </span>
              <h2 class="text-3xl font-bold text-white">Service Desk & ITSM Skills Diagnostic</h2>
              <p class="text-slate-300 text-xs max-w-2xl">Evaluate your operational knowledge across 6 key competencies: Customer Communication, Ticket Documentation, ITIL Concepts, Technical Troubleshooting, XLAs, and AI Awareness.</p>
            </div>
            <div class="p-4 glass-panel border border-white/[0.08] rounded-2xl text-center shrink-0 min-w-[140px]">
              <span id="diag-progress-text" class="text-xl font-extrabold text-cyberCyan block font-mono">0 / 25 Answered</span>
              <div class="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden mt-2">
                <div id="diag-progress-bar" class="h-full bg-gradient-to-r from-cyberCyan to-cyberPurple transition-all duration-300" style="width: 0%;"></div>
              </div>
            </div>
          </div>

          <!-- 25 Questions Container -->
          <div id="diagnostic-questions-container" class="space-y-4 pt-4">
            <!-- Populated by skills_diagnostic_engine.js -->
          </div>

          <div class="pt-6 border-t border-slate-800 flex justify-between items-center">
            <span class="text-xs text-slate-400 font-mono">Takes approx. 8-10 minutes to complete</span>
            <button onclick="submitDiagnosticQuiz()" class="cyber-btn px-8 py-3 text-xs font-bold flex items-center gap-2">
              <i class="fa-solid fa-chart-pie"></i> Calculate Diagnostic Scorecard
            </button>
          </div>
        </div>
      </section>

      <!-- ==================== SOP TEMPLATES TAB ==================== -->
      <section id="tab-templates" class="tab-view hidden space-y-8 max-w-6xl mx-auto">
        <div class="glass-panel p-8 space-y-6 rounded-3xl border border-emerald-400/30">
          <div class="space-y-2">
            <span class="px-3.5 py-1.5 rounded-full text-xs font-bold bg-emerald-400/10 border border-emerald-400/30 text-emerald-400 inline-flex items-center gap-2">
              <i class="fa-solid fa-file-signature"></i> Original Operating Playbooks
            </span>
            <h2 class="text-3xl font-bold text-white">Downloadable ITIL SOP & Templates Library</h2>
            <p class="text-slate-300 text-xs max-w-2xl">Production-tested templates, quality scorecards, and incident playbooks designed from 20+ years of operational IT leadership.</p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Template 1 -->
            <div class="glass-panel p-5 space-y-3 rounded-2xl border border-white/[0.08] hover:border-emerald-400/50 transition">
              <div class="w-10 h-10 rounded-xl bg-emerald-400/10 border border-emerald-400/30 text-emerald-400 flex items-center justify-center text-lg">
                <i class="fa-solid fa-list-check"></i>
              </div>
              <h3 class="font-bold text-white text-sm">Incident Ticket Quality Scorecard</h3>
              <p class="text-slate-400 text-xs">Audit rubric evaluating caller verification, work notes quality, CTI tagging, and resolution summaries.</p>
              <button onclick="downloadSOPTemplate('ticket_quality')" class="cyber-btn-outline w-full py-2 text-xs font-bold flex items-center justify-center gap-2">
                <i class="fa-solid fa-download"></i> Download SOP Checklist (PDF)
              </button>
            </div>

            <!-- Template 2 -->
            <div class="glass-panel p-5 space-y-3 rounded-2xl border border-white/[0.08] hover:border-cyberCyan/50 transition">
              <div class="w-10 h-10 rounded-xl bg-cyberCyan/10 border border-cyberCyan/30 text-cyberCyan flex items-center justify-center text-lg">
                <i class="fa-solid fa-table-cells"></i>
              </div>
              <h3 class="font-bold text-white text-sm">Impact x Urgency Priority Matrix</h3>
              <p class="text-slate-400 text-xs">Standardized decision table to classify P1 Critical outages vs P4 Low service requests objectively.</p>
              <button onclick="downloadSOPTemplate('priority_matrix')" class="cyber-btn-outline w-full py-2 text-xs font-bold flex items-center justify-center gap-2">
                <i class="fa-solid fa-download"></i> Download Matrix (PDF)
              </button>
            </div>

            <!-- Template 3 -->
            <div class="glass-panel p-5 space-y-3 rounded-2xl border border-white/[0.08] hover:border-red-500/50 transition">
              <div class="w-10 h-10 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 flex items-center justify-center text-lg">
                <i class="fa-solid fa-bullhorn"></i>
              </div>
              <h3 class="font-bold text-white text-sm">P1 Major Incident War Room Playbook</h3>
              <p class="text-slate-400 text-xs">Executive status update broadcasts, bridge call agendas, and emergency CAB escalation templates.</p>
              <button onclick="downloadSOPTemplate('p1_playbook')" class="cyber-btn-outline w-full py-2 text-xs font-bold flex items-center justify-center gap-2">
                <i class="fa-solid fa-download"></i> Download Playbook (DOCX)
              </button>
            </div>

            <!-- Template 4 -->
            <div class="glass-panel p-5 space-y-3 rounded-2xl border border-white/[0.08] hover:border-cyberPurple/50 transition">
              <div class="w-10 h-10 rounded-xl bg-cyberPurple/10 border border-cyberPurple/30 text-cyberPurple flex items-center justify-center text-lg">
                <i class="fa-solid fa-arrow-right-arrow-left"></i>
              </div>
              <h3 class="font-bold text-white text-sm">Shift Handover & Operations Log</h3>
              <p class="text-slate-400 text-xs">Structured daily operational log ensuring seamless transfer of open P2/P3 incidents between shifts.</p>
              <button onclick="downloadSOPTemplate('shift_handover')" class="cyber-btn-outline w-full py-2 text-xs font-bold flex items-center justify-center gap-2">
                <i class="fa-solid fa-download"></i> Download Log Template (XLSX)
              </button>
            </div>

            <!-- Template 5 -->
            <div class="glass-panel p-5 space-y-3 rounded-2xl border border-white/[0.08] hover:border-amber-400/50 transition">
              <div class="w-10 h-10 rounded-xl bg-amber-400/10 border border-amber-400/30 text-amber-400 flex items-center justify-center text-lg">
                <i class="fa-solid fa-diagram-project"></i>
              </div>
              <h3 class="font-bold text-white text-sm">5-Why Root Cause Analysis (RCA) Worksheet</h3>
              <p class="text-slate-400 text-xs">Post-Incident Review (PIR) template to drill down from system symptom to permanent corrective action.</p>
              <button onclick="downloadSOPTemplate('rca_worksheet')" class="cyber-btn-outline w-full py-2 text-xs font-bold flex items-center justify-center gap-2">
                <i class="fa-solid fa-download"></i> Download RCA Worksheet (DOCX)
              </button>
            </div>

            <!-- Template 6 -->
            <div class="glass-panel p-5 space-y-3 rounded-2xl border border-white/[0.08] hover:border-cyberCyan/50 transition">
              <div class="w-10 h-10 rounded-xl bg-cyberCyan/10 border border-cyberCyan/30 text-cyberCyan flex items-center justify-center text-lg">
                <i class="fa-solid fa-book-bookmark"></i>
              </div>
              <h3 class="font-bold text-white text-sm">KCS Knowledge Article Drafting Template</h3>
              <p class="text-slate-400 text-xs">Standard Knowledge-Centered Service layout with Problem, Environment, Cause, and Solution sections.</p>
              <button onclick="downloadSOPTemplate('kcs_template')" class="cyber-btn-outline w-full py-2 text-xs font-bold flex items-center justify-center gap-2">
                <i class="fa-solid fa-download"></i> Download KCS Template (DOCX)
              </button>
            </div>
          </div>
        </div>
      </section>
"""

if 'id="tab-diagnostic"' not in html:
    html = html.replace('<!-- ==================== COURSES (FREE) MULTI-TRACK TAB ==================== -->', f'{diagnostic_tab_html}\n<!-- ==================== COURSES (FREE) MULTI-TRACK TAB ==================== -->')

# 9. Add Diagnostic Scorecard Modal HTML (`#diagnostic-results-modal`)
diagnostic_modal_html = """
  <!-- Diagnostic Scorecard Results Modal -->
  <div id="diagnostic-results-modal" class="fixed inset-0 bg-cyberBg/95 backdrop-blur-md z-[9999] flex items-center justify-center p-4 hidden transition-all duration-300 opacity-0">
    <div class="glass-panel w-full max-w-2xl flex flex-col bg-gradient-to-br from-cyberSlate to-cyberBg border border-cyberCyan/40 overflow-hidden shadow-2xl relative rounded-2xl">
      <div class="p-5 border-b border-slate-800 flex justify-between items-center bg-black/50 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-cyberCyan/20 border border-cyberCyan/30 flex items-center justify-center text-cyberCyan text-lg shrink-0">
            <i class="fa-solid fa-chart-pie"></i>
          </div>
          <div>
            <span class="px-2 py-0.5 rounded bg-cyberCyan/20 text-cyberCyan text-[9px] font-mono font-bold uppercase border border-cyberCyan/30">SKILLS SCORECARD</span>
            <h3 class="font-bold text-base text-white mt-0.5">Your ITSM Diagnostic Scorecard</h3>
          </div>
        </div>
        <button onclick="closeDiagnosticResultsModal()" class="w-9 h-9 rounded-lg bg-white/[0.05] border border-white/[0.08] flex items-center justify-center text-slate-400 hover:text-white transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <div class="p-6 space-y-6 overflow-y-auto max-h-[80vh]">
        <div class="text-center space-y-3 p-6 bg-black/40 border border-slate-800 rounded-2xl">
          <span class="text-xs font-mono text-slate-400 uppercase tracking-widest block">Overall Score</span>
          <span id="diag-score-val" class="text-4xl font-extrabold text-cyberCyan font-mono">0% (0/25)</span>
          <div id="diag-level-rec" class="mt-2"></div>
        </div>

        <div class="space-y-3">
          <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider font-mono">Competency Breakdown</h4>
          <div id="diag-breakdown-container" class="space-y-2"></div>
        </div>
      </div>

      <div class="p-4 border-t border-slate-800 bg-black/50 shrink-0 flex justify-between items-center">
        <button onclick="switchTab('course'); closeDiagnosticResultsModal();" class="cyber-btn py-2 px-6 text-xs font-bold">
          Start Recommended Learning Level
        </button>
        <button onclick="closeDiagnosticResultsModal()" class="cyber-btn-outline py-2 px-4 text-xs font-bold">
          Close Scorecard
        </button>
      </div>
    </div>
  </div>
"""

if 'id="diagnostic-results-modal"' not in html:
    html = html.replace('<!-- Interactive Chapter Studio Modal -->', f'{diagnostic_modal_html}\n<!-- Interactive Chapter Studio Modal -->')

# 10. Add Trust Center Modal HTML (`#trust-center-modal`)
trust_center_modal_html = """
  <!-- Trust Center & Governance Modal -->
  <div id="trust-center-modal" class="fixed inset-0 bg-cyberBg/95 backdrop-blur-md z-[9999] flex items-center justify-center p-4 hidden transition-all duration-300 opacity-0">
    <div class="glass-panel w-full max-w-4xl max-h-[90vh] flex flex-col bg-gradient-to-br from-cyberSlate to-cyberBg border border-white/[0.15] overflow-hidden shadow-2xl relative rounded-2xl">
      <div class="p-5 border-b border-slate-800 flex justify-between items-center bg-black/50 shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-emerald-400/20 border border-emerald-400/30 flex items-center justify-center text-emerald-400 text-lg shrink-0">
            <i class="fa-solid fa-shield-halved"></i>
          </div>
          <div>
            <span class="px-2 py-0.5 rounded bg-emerald-400/20 text-emerald-400 text-[9px] font-mono font-bold uppercase border border-emerald-400/30">GOVERNANCE & TRUST</span>
            <h3 class="font-bold text-base text-white mt-0.5">AI-ITSM Hub Trust Center</h3>
          </div>
        </div>
        <button onclick="closeTrustCenterModal()" class="w-9 h-9 rounded-lg bg-white/[0.05] border border-white/[0.08] flex items-center justify-center text-slate-400 hover:text-white transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <div class="flex border-b border-slate-800 bg-black/40 text-xs font-mono px-4 overflow-x-auto shrink-0">
        <button onclick="switchTrustTab('privacy')" id="trust-tab-btn-privacy" class="px-4 py-3 border-b-2 border-cyberCyan text-cyberCyan font-bold">Privacy Notice</button>
        <button onclick="switchTrustTab('cookie')" id="trust-tab-btn-cookie" class="px-4 py-3 border-b-2 border-transparent text-slate-400 hover:text-white">Cookie Policy</button>
        <button onclick="switchTrustTab('terms')" id="trust-tab-btn-terms" class="px-4 py-3 border-b-2 border-transparent text-slate-400 hover:text-white">Terms of Use</button>
        <button onclick="switchTrustTab('aipolicy')" id="trust-tab-btn-aipolicy" class="px-4 py-3 border-b-2 border-transparent text-slate-400 hover:text-white">AI Safety Policy</button>
        <button onclick="switchTrustTab('certpolicy')" id="trust-tab-btn-certpolicy" class="px-4 py-3 border-b-2 border-transparent text-slate-400 hover:text-white">Certificate Policy</button>
      </div>

      <div class="p-6 space-y-4 overflow-y-auto flex-1 text-xs text-slate-300 leading-relaxed font-mono">
        <div id="trust-view-privacy" class="space-y-3">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">Privacy Notice & Personal Data Handling (ICO Aligned)</h4>
          <p>AI-ITSM Hub collects personal data submitted through contact forms (Name, Email, Message) solely for responding to consulting inquiries and platform support. We process personal data under Legitimate Interest and Consent under UK GDPR and Data Protection Act 2018 standards.</p>
          <p><strong>Data Retention:</strong> Contact submissions are retained for up to 12 months and never sold to third parties.</p>
        </div>

        <div id="trust-view-cookie" class="space-y-3 hidden">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">Cookie Policy</h4>
          <p>This platform uses strictly necessary local storage cookies to remember your course progress, diagnostic quiz history, and navigation preferences. No intrusive tracking or advertising cookies are utilized.</p>
        </div>

        <div id="trust-view-terms" class="space-y-3 hidden">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">Terms of Use & Intellectual Property</h4>
          <p>All educational materials, SOP templates, diagnostic tools, and software code hosted on AI-ITSM Hub are provided for individual professional learning. Redistribution or commercial resale without written consent is prohibited.</p>
        </div>

        <div id="trust-view-aipolicy" class="space-y-3 hidden">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">AI Safety & Governance Policy (NCSC / OWASP Aligned)</h4>
          <p>AI tools on this platform operate on synthetic training data. Users MUST NOT enter confidential patient data, real credentials, or production corporate secrets into AI prompts. All AI outputs serve as recommendations requiring human-in-the-loop review.</p>
        </div>

        <div id="trust-view-certpolicy" class="space-y-3 hidden">
          <h4 class="text-sm font-bold text-white uppercase tracking-wider">Independent Certificate Policy</h4>
          <p>Certificates of Completion issued by AI-ITSM Hub represent independent practitioner skills attainment evaluated via scenario examinations. They do NOT constitute official accreditation from PeopleCert, Axelos, ITIL, or external awarding bodies.</p>
        </div>
      </div>

      <div class="p-4 border-t border-slate-800 bg-black/50 shrink-0 flex justify-between items-center">
        <span class="text-[10px] text-slate-500 font-mono">AI-ITSM Hub Governance • Last Reviewed: August 2026</span>
        <button onclick="closeTrustCenterModal()" class="cyber-btn py-2 px-6 text-xs font-bold">
          I Understand / Close
        </button>
      </div>
    </div>
  </div>
"""

if 'id="trust-center-modal"' not in html:
    html = html.replace('</body>', f'{trust_center_modal_html}\n</body>')

# 11. Add Trust Links to Footer in main layout
footer_trust_html = """
      <!-- Governance & Trust Footer -->
      <footer class="mt-16 pt-8 border-t border-white/[0.08] flex flex-col md:flex-row justify-between items-center gap-4 text-xs font-mono text-slate-400">
        <div>
          <p>© 2026 AI-ITSM Hub • Led by Abhineet Singh (20+ Years IT Operations Leader)</p>
          <p class="text-[10px] text-slate-500 mt-0.5">Independent ITSM Learning & AI Automation Platform</p>
        </div>
        <div class="flex flex-wrap gap-4">
          <a href="#" onclick="openTrustCenterModal('privacy')" class="hover:text-cyberCyan transition">Privacy Notice</a>
          <span>•</span>
          <a href="#" onclick="openTrustCenterModal('cookie')" class="hover:text-cyberCyan transition">Cookie Policy</a>
          <span>•</span>
          <a href="#" onclick="openTrustCenterModal('terms')" class="hover:text-cyberCyan transition">Terms of Use</a>
          <span>•</span>
          <a href="#" onclick="openTrustCenterModal('aipolicy')" class="hover:text-cyberCyan transition">AI Policy</a>
          <span>•</span>
          <a href="#" onclick="openTrustCenterModal('certpolicy')" class="hover:text-cyberCyan transition">Certificate Disclaimer</a>
        </div>
      </footer>
"""

if '<!-- Governance & Trust Footer -->' not in html:
    html = html.replace('</main>', f'{footer_trust_html}\n</main>')

# 12. Add JavaScript handlers for Trust Center, Hash Routing & Templates Download
js_blueprint_handlers = """
    // Hash-based SPA Navigation Router
    function handleHashRouting() {
      const hash = window.location.hash.replace('#/', '').replace('#', '');
      if (hash && ['home', 'about', 'services', 'diagnostic', 'templates', 'course', 'ai-sandbox', 'blog', 'forum', 'youtube', 'resources', 'contact'].includes(hash)) {
        switchTab(hash);
      }
    }

    window.addEventListener('hashchange', handleHashRouting);

    function openTrustCenterModal(tabKey = 'privacy') {
      switchTrustTab(tabKey);
      const modal = document.getElementById('trust-center-modal');
      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        setTimeout(() => modal.classList.remove('opacity-0'), 10);
      }
    }

    function closeTrustCenterModal() {
      const modal = document.getElementById('trust-center-modal');
      if (modal) {
        modal.classList.add('opacity-0');
        setTimeout(() => {
          modal.classList.add('hidden');
          modal.classList.remove('flex');
        }, 300);
      }
    }

    function switchTrustTab(key) {
      ['privacy', 'cookie', 'terms', 'aipolicy', 'certpolicy'].forEach(k => {
        const btn = document.getElementById('trust-tab-btn-' + k);
        const view = document.getElementById('trust-view-' + k);
        if (btn) {
          btn.className = "px-4 py-3 border-b-2 border-transparent text-slate-400 hover:text-white";
        }
        if (view) view.classList.add('hidden');
      });

      const activeBtn = document.getElementById('trust-tab-btn-' + key);
      const activeView = document.getElementById('trust-view-' + key);
      if (activeBtn) activeBtn.className = "px-4 py-3 border-b-2 border-cyberCyan text-cyberCyan font-bold";
      if (activeView) activeView.classList.remove('hidden');
    }

    function downloadSOPTemplate(templateKey) {
      alert(`📄 Downloading Official SOP Template (${templateKey.toUpperCase()}) prepared by Abhineet Singh...`);
    }
"""

if 'handleHashRouting' not in html:
    html = html.replace(
        'document.addEventListener(\'DOMContentLoaded\', () => {',
        f'{js_blueprint_handlers.strip()}\n\n    document.addEventListener(\'DOMContentLoaded\', () => {{\n      handleHashRouting();'
    )

# Link skills_diagnostic_engine.js before closing body
if 'skills_diagnostic_engine.js' not in html:
    html = html.replace('</body>', '  <script src="skills_diagnostic_engine.js"></script>\n</body>')

index_path.write_text(html, encoding="utf-8")
print("[OK] Rebuilt index.html with Executive Blueprint upgrades, Trust Center, Skills Diagnostic & Hash Routing!")
