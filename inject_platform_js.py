import re
from pathlib import Path

WORKSPACE_DIR = Path("C:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")
INDEX_PATH = WORKSPACE_DIR / "index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Add script block before </body>
js_platform_engine = """
<script>
// -------------------------------------------------------------
// COURSE CHAPTERS DATA (12 Chapters in 3 Progression Levels)
// -------------------------------------------------------------
const platformCourseChapters = [
    // LEVEL 1: FOUNDATION (Chapters 1-4)
    {
        id: "ch_1", chapterNum: 1, level: 1, levelName: "Level 1: Foundation",
        title: "Modern IT Service Desk Fundamentals", duration: "45 min", badge: "Helpdesk Basics",
        desc: "Role of Service Desk, Call vs. Ticket Logging, Active Listening, Customer Centricity, First Contact Resolution (FCR).",
        keyTakeaways: [
            "Difference between Helpdesk, Service Desk & ITSM",
            "Active Listening & empathetic user communication",
            "FCR (First Contact Resolution) optimization metrics",
            "Standard Ticket Logging fields (Caller, Impact, Urgency)"
        ]
    },
    {
        id: "ch_2", chapterNum: 2, level: 1, levelName: "Level 1: Foundation",
        title: "Incident Management Basics & Ticket Lifecycle", duration: "50 min", badge: "Incident Mgt",
        desc: "Incident Definition vs Request, Priority Matrix (Impact x Urgency), Ticket Statuses, Work Notes & Audit Trails.",
        keyTakeaways: [
            "Incident vs. Service Request distinction",
            "Priority Matrix calculation (P1 Critical vs P4 Low)",
            "Ticket Lifecycle: New -> In Progress -> On Hold -> Resolved",
            "Effective Work Notes for L2/L3 escalation"
        ]
    },
    {
        id: "ch_3", chapterNum: 3, level: 1, levelName: "Level 1: Foundation",
        title: "Identity, Access & Active Directory Management", duration: "40 min", badge: "Active Directory",
        desc: "Active Directory (AD) User Creation, Password Resets, Locked Accounts, Security Groups, Multi-Factor Authentication (MFA).",
        keyTakeaways: [
            "AD Users, OUs & Security Group memberships",
            "Password unlock & reset troubleshooting procedures",
            "MFA (Microsoft Authenticator) registration & reset",
            "Shared Folder & Network Drive security permissions"
        ]
    },
    {
        id: "ch_4", chapterNum: 4, level: 1, levelName: "Level 1: Foundation",
        title: "Customer Communication & SLA Management", duration: "35 min", badge: "SLAs & Comms",
        desc: "Escalation Etiquette, Managing Anxious Users, SLA Clock Management, Resolution Code Tagging.",
        keyTakeaways: [
            "De-escalating agitated users over phone and chat",
            "SLA Response vs SLA Resolution time clocks",
            "Proper ticket resolution summaries for end-users",
            "CSAT (Customer Satisfaction) survey best practices"
        ]
    },

    // LEVEL 2: INTERMEDIATE (Chapters 5-8)
    {
        id: "ch_5", chapterNum: 5, level: 2, levelName: "Level 2: Intermediate",
        title: "Endpoint Management with MS Intune & VDI", duration: "60 min", badge: "Intune & Endpoints",
        desc: "Intune Device Enrollment, Remote Wipes, Software Deployment, Citrix/VDI Virtual Desktops, Reimaging Laptops.",
        keyTakeaways: [
            "Windows 10/11 Autopilot & Intune enrolment",
            "Remote lock, wipe, and passcode reset operations",
            "Software pushed via Company Portal",
            "Virtual Desktop Infrastructure (Citrix / Windows 365)"
        ]
    },
    {
        id: "ch_6", chapterNum: 6, level: 2, levelName: "Level 2: Intermediate",
        title: "Clinical & Enterprise Application Support", duration: "55 min", badge: "Apps & Clinical",
        desc: "EMIS Web, SystmOne, NHS Mail administration, MS Teams, SharePoint permissions, Application crash diagnostics.",
        keyTakeaways: [
            "EMIS Web & SystmOne credential & access reset",
            "NHS Mail admin portal & shared mailboxes",
            "Troubleshooting Teams, Outlook & Office 365 crashes",
            "Log collection & application event viewer analysis"
        ]
    },
    {
        id: "ch_7", chapterNum: 7, level: 2, levelName: "Level 2: Intermediate",
        title: "Joiners, Movers, Leavers (JML) & Smartcards (RA)", duration: "50 min", badge: "JML & Smartcards",
        desc: "Automated JML Workflows, Hardware Provisioning, NHS Smartcard (RA) unlocking, renewals, spine roles.",
        keyTakeaways: [
            "Day 1 Readiness for Joiner onboarding",
            "Mover role transfer & access revocation",
            "Leaver hardware retrieval & account disablement",
            "RA Smartcard passcode reset & Spine role assignment"
        ]
    },
    {
        id: "ch_8", chapterNum: 8, level: 2, levelName: "Level 2: Intermediate",
        title: "Major Incident Management & CAB Approvals", duration: "65 min", badge: "P1 Incidents & CAB",
        desc: "P1/P2 Major Incident Bridge Calls, Root Cause Analysis (RCA), CAB approvals, Risk Assessment for Changes.",
        keyTakeaways: [
            "Declaring P1 Major Incidents & running outage bridges",
            "Status page broadcasts & stakeholder communication",
            "Emergency vs Standard vs Normal CAB Changes",
            "Post-Incident Review (PIR) & Root Cause Analysis (RCA)"
        ]
    },

    // LEVEL 3: ADVANCED (Chapters 9-12)
    {
        id: "ch_9", chapterNum: 9, level: 3, levelName: "Level 3: Advanced ITIL & AI",
        title: "Shift-Left Strategy & Knowledge Engineering", duration: "60 min", badge: "Shift-Left & KCS",
        desc: "KCS (Knowledge-Centered Service), Self-Service Deflection, Knowledge Base (KB) Article Publishing, End-User Empowering.",
        keyTakeaways: [
            "Shift-Left concept: L2 -> L1 -> Self-Service AI",
            "KCS Article drafting & review workflow",
            "Designing user-friendly KB guides with screenshots",
            "Measuring deflection rate & self-service adoption"
        ]
    },
    {
        id: "ch_10", chapterNum: 10, level: 3, levelName: "Level 3: Advanced ITIL & AI",
        title: "Metrics, Scorecards & Experience Level Agreements (XLAs)", duration: "55 min", badge: "XLAs & Scorecards",
        desc: "Shift from SLAs to XLAs (Experience Level Agreements), CSAT Metrics, Analyst Productivity Scorecards, Weightage Systems.",
        keyTakeaways: [
            "Why traditional SLAs fail end-user satisfaction",
            "Designing XLAs (Sentiment, Ease of Use, Employee Productivity)",
            "Creating Analyst Productivity Scorecards",
            "Gamification & Recognition (Hall of Fame)"
        ]
    },
    {
        id: "ch_11", chapterNum: 11, level: 3, levelName: "Level 3: Advanced ITIL & AI",
        title: "ITSM Tool Deep Dive: ServiceNow vs. Halo ESM", duration: "70 min", badge: "ServiceNow & Halo",
        desc: "Halo ESM Configuration, ServiceNow Workflows, Catalog Management, ESM expansion beyond IT.",
        keyTakeaways: [
            "Architecture comparison: ServiceNow vs Halo ESM",
            "Configuring Service Catalogs & Request Workflows",
            "Enterprise Service Management (ESM for HR, Facilities, Finance)",
            "Cost optimization & ROI calculation for ITSM platforms"
        ]
    },
    {
        id: "ch_12", chapterNum: 12, level: 3, levelName: "Level 3: Advanced ITIL & AI",
        title: "Next-Gen AI Service Desk & Virtual Agent Integration", duration: "80 min", badge: "AI Virtual Agent",
        desc: "Building Zero-Touch AI Agents, LLM Intent Classification, Automated Ticket Triage, LangChain/CrewAI Workflows.",
        keyTakeaways: [
            "AI Agent architecture for IT Helpdesk support",
            "Natural Language Intent Classification for tickets",
            "Connecting RAG Knowledge Base to LLM chatbots",
            "Automated resolution of L1 password & access requests"
        ]
    }
];

function renderPlatformCourseChapters(filterLvl = 'all') {
    const grid = document.getElementById('course-chapters-grid');
    if (!grid) return;
    grid.innerHTML = '';

    const filtered = filterLvl === 'all' 
        ? platformCourseChapters 
        : platformCourseChapters.filter(c => c.level === parseInt(filterLvl));

    filtered.forEach(ch => {
        const card = document.createElement('div');
        card.className = 'glass-panel p-6 flex flex-col justify-between space-y-4 hover:border-cyberCyan/40 transition duration-300 relative';
        
        let chipBg = 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30';
        if (ch.level === 2) chipBg = 'bg-cyberBlue/20 text-cyberBlue border-cyberBlue/30';
        if (ch.level === 3) chipBg = 'bg-cyberPurple/20 text-cyberPurple border-cyberPurple/30';

        const takeaways = ch.keyTakeaways.map(t => `<li class="flex items-start gap-1.5"><i class="fa-solid fa-circle-check text-[10px] text-cyberCyan mt-1"></i> <span>${t}</span></li>`).join('');

        card.innerHTML = `
            <div class="space-y-3">
                <div class="flex justify-between items-center text-xs">
                    <span class="px-2.5 py-0.5 rounded text-[10px] font-bold border uppercase ${chipBg}">${ch.levelName}</span>
                    <span class="font-mono text-[10px] text-slate-500">Chapter ${ch.chapterNum} of 12</span>
                </div>
                <h3 class="text-base font-bold text-white leading-snug">${ch.title}</h3>
                <p class="text-slate-400 text-xs leading-relaxed">${ch.desc}</p>
                <div class="flex flex-wrap gap-2 pt-1 font-mono text-[10px]">
                    <span class="px-2 py-0.5 bg-white/[0.04] border border-white/[0.08] rounded text-slate-300"><i class="fa-regular fa-clock text-amber-400"></i> ${ch.duration}</span>
                    <span class="px-2 py-0.5 bg-white/[0.04] border border-white/[0.08] rounded text-slate-300"><i class="fa-solid fa-tag text-cyberCyan"></i> ${ch.badge}</span>
                </div>
                <div class="p-3 bg-black/40 border border-slate-800 rounded-xl space-y-2">
                    <span class="text-[10px] font-bold text-cyberPurple uppercase tracking-wider block"><i class="fa-solid fa-lightbulb"></i> Key Takeaways</span>
                    <ul class="space-y-1 text-xs text-slate-300 font-mono">${takeaways}</ul>
                </div>
            </div>
            <div class="flex gap-2 pt-2">
                <button onclick="openChapterLessonModal('${ch.title}', '${ch.duration}')" class="cyber-btn text-xs py-2 flex-1 justify-center"><i class="fa-solid fa-circle-play"></i> Watch Lesson</button>
                <button onclick="openContactModalWithSubject('Question: ${ch.title}')" class="cyber-btn-outline text-xs py-2 px-3"><i class="fa-solid fa-envelope"></i> Ask</button>
            </div>
        `;
        grid.appendChild(card);
    });
}

function filterCourseLevel(lvl) {
    document.querySelectorAll('.course-lvl-btn').forEach(btn => {
        btn.classList.remove('bg-amber-500', 'text-white', 'shadow-lg');
        btn.classList.add('bg-white/[0.03]', 'text-slate-400');
    });
    const activeBtn = document.getElementById(`btn-lvl-${lvl}`);
    if (activeBtn) {
        activeBtn.classList.remove('bg-white/[0.03]', 'text-slate-400');
        activeBtn.classList.add('bg-amber-500', 'text-white', 'shadow-lg');
    }
    renderPlatformCourseChapters(lvl);
}

function openChapterLessonModal(title, duration) {
    alert(`🎓 ${title} (${duration})\\n\\nThis lesson script is ready! Have questions about this chapter? Click 'Ask' to email Abhineet directly.`);
}

function copyDirectEmail() {
    navigator.clipboard.writeText('abhineetsam2027@gmail.com');
    showPlatformToast('Copied email: abhineetsam2027@gmail.com');
}

function openContactModalWithSubject(subject) {
    switchTab('contact');
    const subjInput = document.getElementById('contact-subject');
    if (subjInput) subjInput.value = 'ITSM Integration';
    const msgInput = document.getElementById('contact-message');
    if (msgInput) msgInput.value = `Hi Abhineet,\\n\\n${subject}\\n\\n[Write your question here...]`;
}

function showPlatformToast(msg) {
    const toast = document.createElement('div');
    toast.className = 'fixed bottom-6 right-6 bg-emerald-500 text-white px-5 py-3 rounded-xl font-bold text-xs shadow-2xl z-[10000] flex items-center gap-2 animate-bounce';
    toast.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${msg}`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

// Initial course render
document.addEventListener('DOMContentLoaded', () => {
    renderPlatformCourseChapters('all');
});
</script>
"""

# Replace switchTab function to include course view handling
if 'function switchTab(' in html:
    old_switch = """function switchTab(tabId) {"""
    new_switch = """function switchTab(tabId) {
      if (tabId === 'course') {
        renderPlatformCourseChapters('all');
      }"""
    html = html.replace(old_switch, new_switch, 1)

if '</body>' in html and 'renderPlatformCourseChapters' not in html:
    html = html.replace('</body>', js_platform_engine + '\n</body>')

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Injected course script engine into index.html successfully!")
