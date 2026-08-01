/**
 * ITSM & Service Desk 25-Question Diagnostic Engine
 * Created for AI-ITSM Hub | Abhineet Singh
 */

const diagnosticQuestions = [
  // Category 1: Customer Communication & De-escalation (Qs 1-4)
  {
    id: 1,
    category: "Communication",
    categoryName: "Customer Communication & Empathy",
    question: "An anxious clinical user calls stating their EMIS Web application crashed mid-consultation. What is your immediate first response?",
    options: [
      "Ask them to restart their computer immediately without listening.",
      "Acknowledge the stress, verify user identity calmly, and assure them you are taking ownership to resolve it.",
      "Tell them to log a ticket on the self-service portal and hang up.",
      "Escalate immediately to the infrastructure team without taking details."
    ],
    correctIndex: 1,
    explanation: "Empathy and active ownership de-escalate anxiety while capturing vital incident context for rapid resolution."
  },
  {
    id: 2,
    category: "Communication",
    categoryName: "Customer Communication & Empathy",
    question: "When sending an incident resolution update to a high-priority executive, what is the best format?",
    options: [
      "Send a 10-page raw technical log file.",
      "Send a clear 3-bullet executive summary: Business Impact, Resolution Action, and Preventative Steps.",
      "Do not communicate until the monthly SLA report is published.",
      "Send a quick text message saying 'fixed'."
    ],
    correctIndex: 1,
    explanation: "Executive communications require concise, business-focused summaries highlighting impact and preventative measures."
  },
  {
    id: 3,
    category: "Communication",
    categoryName: "Customer Communication & Empathy",
    question: "What is the primary objective of First Contact Resolution (FCR)?",
    options: [
      "To resolve the user's issue during the initial call/chat without transferring or reopening.",
      "To close as many tickets as possible regardless of resolution quality.",
      "To force users to use self-service chatbots only.",
      "To keep the phone call duration under 60 seconds."
    ],
    correctIndex: 0,
    explanation: "FCR measures tickets resolved on first contact, minimizing user downtime and operational effort."
  },
  {
    id: 4,
    category: "Communication",
    categoryName: "Customer Communication & Empathy",
    question: "How should an analyst handle an angry user shouting about recurring system slowness?",
    options: [
      "Shout back to assert authority.",
      "Interrupt them mid-sentence to give technical explanation.",
      "Listen actively without interrupting, validate their frustration, and focus on immediate troubleshooting steps.",
      "Put the user on hold indefinitely."
    ],
    correctIndex: 2,
    explanation: "Active listening and emotional validation neutralize hostility, turning conflict into collaborative problem-solving."
  },

  // Category 2: Ticket Documentation & Quality (Qs 5-8)
  {
    id: 5,
    category: "Documentation",
    categoryName: "Ticket Quality & Work Notes",
    question: "What essential information MUST be recorded in a Service Desk incident work note before escalating to L2?",
    options: [
      "Only the user's phone number.",
      "Caller identity, detailed symptom, error codes, steps already attempted, and exact reproduction steps.",
      "A note saying 'Escalated to L2'.",
      "No notes are needed if transferred orally."
    ],
    correctIndex: 1,
    explanation: "Comprehensive ticket notes eliminate duplicate troubleshooting and reduce total resolution time (MTTR)."
  },
  {
    id: 6,
    category: "Documentation",
    categoryName: "Ticket Quality & Work Notes",
    question: "Why is correct CTI (Category, Type, Item) taxonomy tagging critical?",
    options: [
      "It makes the ticket look colorful.",
      "It enables accurate automated routing, trend analysis, and root cause identification.",
      "It is only used for billing users.",
      "It increases analyst typing speed."
    ],
    correctIndex: 1,
    explanation: "Accurate CTI tagging drives intelligent ticket routing, SLA tracking, and automated AI trend detection."
  },
  {
    id: 7,
    category: "Documentation",
    categoryName: "Ticket Quality & Work Notes",
    question: "What is the difference between Internal Work Notes and Customer Visible Comments?",
    options: [
      "They are identical and seen by everyone.",
      "Work notes contain internal technical details/logs for engineers; Customer comments are end-user friendly updates.",
      "Work notes are seen by the customer; Customer comments are private.",
      "Neither is stored in the ITSM tool audit log."
    ],
    correctIndex: 1,
    explanation: "Segregating internal engineering notes from public customer updates maintains professionalism and data security."
  },
  {
    id: 8,
    category: "Documentation",
    categoryName: "Ticket Quality & Work Notes",
    question: "When closing an incident, what is a mandatory requirement for the Resolution Summary?",
    options: [
      "Type 'done' or 'fixed'.",
      "Document the root cause found, fix applied, verified user confirmation, and appropriate resolution code tag.",
      "Leave the summary blank.",
      "Paste the entire Windows registry file."
    ],
    correctIndex: 1,
    explanation: "Clear resolution summaries feed Knowledge Management (KCS) databases and allow self-healing AI training."
  },

  // Category 3: ITIL Framework & Incident Lifecycle (Qs 9-12)
  {
    id: 9,
    category: "ITIL",
    categoryName: "ITIL Framework & Incident Lifecycle",
    question: "In ITIL 4, what is the official definition of an Incident?",
    options: [
      "A request for a new laptop or software license.",
      "An unplanned interruption to a service or reduction in the quality of a service.",
      "A planned change to network routers.",
      "A routine password reset."
    ],
    correctIndex: 1,
    explanation: "Incidents are unplanned disruptions requiring rapid restoration of normal service operation."
  },
  {
    id: 10,
    category: "ITIL",
    categoryName: "ITIL Framework & Incident Lifecycle",
    question: "How is Incident Priority calculated in ITIL frameworks?",
    options: [
      "Priority = Impact x Urgency",
      "Priority = Analyst Preference + Time of Day",
      "Priority = VIP Status only",
      "Priority = Number of tickets in queue"
    ],
    correctIndex: 0,
    explanation: "Priority is derived objectively by evaluating Impact (number of affected users/services) and Urgency (business deadline)."
  },
  {
    id: 11,
    category: "ITIL",
    categoryName: "ITIL Framework & Incident Lifecycle",
    question: "What distinguishes Problem Management from Incident Management?",
    options: [
      "Incident Management focuses on finding root cause; Problem Management restores service quickly.",
      "Incident Management restores normal service ASAP; Problem Management identifies and eliminates underlying causes.",
      "They are identical processes with different names.",
      "Problem Management only handles hardware repairs."
    ],
    correctIndex: 1,
    explanation: "Incident Management minimizes immediate business disruption, while Problem Management prevents recurring incidents."
  },
  {
    id: 12,
    category: "ITIL",
    categoryName: "ITIL Framework & Incident Lifecycle",
    question: "What is an Emergency Change in Change Enablement (CAB)?",
    options: [
      "A change that must be implemented ASAP to resolve a Major Incident or critical security vulnerability.",
      "A change requested by an analyst on Friday afternoon.",
      "A change that requires 3 weeks of standard documentation.",
      "A software update scheduled 6 months in advance."
    ],
    correctIndex: 0,
    explanation: "Emergency Changes follow streamlined approval workflows to mitigate active high-impact outages safely."
  },

  // Category 4: Technical Troubleshooting & AD Access (Qs 13-16)
  {
    id: 13,
    category: "Troubleshooting",
    categoryName: "Technical Troubleshooting & Access",
    question: "A user cannot access a shared network drive after a department transfer. What is the most likely root cause?",
    options: [
      "The monitor cable is loose.",
      "Active Directory Security Group membership was updated/removed during the move.",
      "The internet router collapsed.",
      "The user's keyboard layout changed."
    ],
    correctIndex: 1,
    explanation: "Shared drive permissions in enterprise Windows environments are governed by Active Directory Security Groups."
  },
  {
    id: 14,
    category: "Troubleshooting",
    categoryName: "Technical Troubleshooting & Access",
    question: "What command line tool checks network latency and packet loss to an IP address or domain?",
    options: [
      "ipconfig /all",
      "ping or pathping",
      "taskmgr",
      "chkdsk"
    ],
    correctIndex: 1,
    explanation: "Ping and Pathping send ICMP echo packets to diagnose network connectivity, latency, and packet loss."
  },
  {
    id: 15,
    category: "Troubleshooting",
    categoryName: "Technical Troubleshooting & Access",
    question: "What is Microsoft Intune primary function in enterprise IT?",
    options: [
      "To send promotional email newsletters.",
      "Cloud-based Mobile Device Management (MDM) and Endpoint Configuration Manager for laptops/mobile devices.",
      "To design graphic presentations.",
      "To manage physical office HVAC systems."
    ],
    correctIndex: 1,
    explanation: "Intune enforces device security policies, remote wipes, app deployment, and compliance for corporate endpoints."
  },
  {
    id: 16,
    category: "Troubleshooting",
    categoryName: "Technical Troubleshooting & Access",
    question: "When performing a Joiner (JML) account setup, why is Role-Based Access Control (RBAC) important?",
    options: [
      "It assigns permissions automatically based on job role, ensuring least-privilege security.",
      "It allows new joiners to access all domain administrator accounts.",
      "It slows down onboarding by 2 weeks.",
      "It disables password enforcement."
    ],
    correctIndex: 0,
    explanation: "RBAC streamlines user onboarding while upholding zero-trust security by granting minimum necessary privileges."
  },

  // Category 5: Metrics, SLAs & XLAs (Qs 17-20)
  {
    id: 17,
    category: "Metrics",
    categoryName: "Metrics, SLAs & XLAs",
    question: "What is the 'Watermelon Effect' in IT Service Management?",
    options: [
      "When tickets turn green on Fridays.",
      "When SLA metrics appear green (compliant) on paper, but user experience/sentiment is red (frustrated).",
      "When a server overheats due to high summer temperatures.",
      "When analysts consume fruits during lunch."
    ],
    correctIndex: 1,
    explanation: "The Watermelon Effect highlights the gap between technical SLA compliance and true end-user satisfaction."
  },
  {
    id: 18,
    category: "Metrics",
    categoryName: "Metrics, SLAs & XLAs",
    question: "How do Experience Level Agreements (XLAs) differ from traditional Service Level Agreements (SLAs)?",
    options: [
      "SLAs measure technical outputs (uptime/MTTR); XLAs measure business outcomes, ease of use, and employee sentiment.",
      "XLAs are legally binding contracts; SLAs are informal notes.",
      "SLAs are for cloud software; XLAs are for physical printers.",
      "They are identical metrics."
    ],
    correctIndex: 0,
    explanation: "XLAs focus on subjective employee experience and productivity rather than rigid system timestamps."
  },
  {
    id: 19,
    category: "Metrics",
    categoryName: "Metrics, SLAs & XLAs",
    question: "What does MTTR stand for in Service Desk performance monitoring?",
    options: [
      "Maximum Time To Record",
      "Mean Time To Resolve",
      "Minimum Transfer Ticket Rate",
      "Managed Technology Team Response"
    ],
    correctIndex: 1,
    explanation: "MTTR calculates the average duration from incident creation to successful resolution."
  },
  {
    id: 20,
    category: "Metrics",
    categoryName: "Metrics, SLAs & XLAs",
    question: "Which metric measures self-service portal effectiveness in preventing phone calls?",
    options: [
      "First Call Resolution",
      "Ticket Deflection Rate",
      "Mean Time Between Failures",
      "Abandonment Rate"
    ],
    correctIndex: 1,
    explanation: "Deflection Rate tracks the percentage of user issues resolved via self-service KB articles or AI virtual agents."
  },

  // Category 6: Responsible AI & Service Desk Automation (Qs 21-25)
  {
    id: 21,
    category: "AI",
    categoryName: "Responsible AI & Automation",
    question: "What is the most critical rule when entering incident work notes into an AI Sandbox or public LLM tool?",
    options: [
      "Paste raw database credentials to get faster answers.",
      "Never enter real passwords, PII, patient health records, or confidential keys; use anonymized examples only.",
      "Always include the caller's home address.",
      "Disable antivirus protection."
    ],
    correctIndex: 1,
    explanation: "Data privacy and AI governance require sanitizing prompts to prevent accidental exposure of confidential enterprise data."
  },
  {
    id: 22,
    category: "AI",
    categoryName: "Responsible AI & Automation",
    question: "What role does Human-in-the-Loop (HITL) oversight play in AI ticket triage?",
    options: [
      "AI makes final decisions automatically without human review.",
      "AI provides recommendations, but human analysts validate and authorize high-risk actions before execution.",
      "Human analysts review AI outputs once per year.",
      "Human analysts type code manually for the AI."
    ],
    correctIndex: 1,
    explanation: "Human oversight ensures AI recommendations undergo expert validation, preventing automated errors or prompt injection risks."
  },
  {
    id: 23,
    category: "AI",
    categoryName: "Responsible AI & Automation",
    question: "How does Retrieval-Augmented Generation (RAG) improve IT Virtual Agent accuracy?",
    options: [
      "It allows the AI to guess answers randomly.",
      "It grounds the AI response in verified, up-to-date internal Knowledge Base (KB) articles and SOPs.",
      "It speeds up typing speed on keyboards.",
      "It replaces human IT Managers entirely."
    ],
    correctIndex: 1,
    explanation: "RAG restricts LLM responses to official internal SOP documentation, eliminating hallucinations."
  },
  {
    id: 24,
    category: "AI",
    categoryName: "Responsible AI & Automation",
    question: "What is 'Shift-Left' strategy powered by AI automation?",
    options: [
      "Moving work from L3 engineers -> L2 -> L1 -> Self-Service AI Agents to resolve issues closer to the end-user.",
      "Shifting analysts to working night shifts.",
      "Moving physical server racks to the left side of the data center.",
      "Canceling all Service Desk shifts."
    ],
    correctIndex: 0,
    explanation: "Shift-Left empowers end-users and L1 analysts with automated tools, reducing resolution costs and wait times."
  },
  {
    id: 25,
    category: "AI",
    categoryName: "Responsible AI & Automation",
    question: "What is 5-Why Root Cause Analysis when assisted by AI?",
    options: [
      "Asking the user 'Why?' 5 times over the phone.",
      "Using structured LLM reasoning to iteratively drill down from symptom to fundamental process/system failure.",
      "Deleting 5 tickets automatically.",
      "Restarting the computer 5 times."
    ],
    correctIndex: 1,
    explanation: "AI-assisted 5-Why analysis systematically traces causal chains to identify actionable preventative measures."
  }
];

let userDiagnosticAnswers = {};

function renderDiagnosticQuiz() {
  const container = document.getElementById('diagnostic-questions-container');
  if (!container) return;

  container.innerHTML = '';

  diagnosticQuestions.forEach((q, idx) => {
    const qCard = document.createElement('div');
    qCard.className = 'glass-panel p-5 space-y-3 rounded-2xl border border-white/[0.08]';
    
    const optionsHtml = q.options.map((opt, oIdx) => `
      <label class="flex items-start gap-3 p-3 bg-black/40 border border-slate-800 rounded-xl cursor-pointer hover:border-cyberCyan/50 transition text-xs text-slate-300">
        <input type="radio" name="diag_q_${q.id}" value="${oIdx}" onchange="recordDiagnosticAnswer(${q.id}, ${oIdx})" class="mt-0.5 accent-cyberCyan">
        <span>${opt}</span>
      </label>
    `).join('');

    qCard.innerHTML = `
      <div class="flex justify-between items-center text-xs">
        <span class="px-2.5 py-0.5 rounded bg-cyberCyan/10 text-cyberCyan border border-cyberCyan/30 font-mono font-bold text-[9px] uppercase">${q.categoryName}</span>
        <span class="font-mono text-[10px] text-slate-400">Question ${idx + 1} of 25</span>
      </div>
      <p class="font-bold text-sm text-white leading-snug">${q.question}</p>
      <div class="space-y-2 pt-1">
        ${optionsHtml}
      </div>
    `;

    container.appendChild(qCard);
  });
}

function recordDiagnosticAnswer(qId, optionIdx) {
  userDiagnosticAnswers[qId] = optionIdx;
  updateDiagnosticProgress();
}

function updateDiagnosticProgress() {
  const answeredCount = Object.keys(userDiagnosticAnswers).length;
  const progressText = document.getElementById('diag-progress-text');
  const progressBar = document.getElementById('diag-progress-bar');

  if (progressText) progressText.textContent = `${answeredCount} / 25 Answered`;
  if (progressBar) progressBar.style.width = `${(answeredCount / 25) * 100}%`;
}

function submitDiagnosticQuiz() {
  const totalAnswered = Object.keys(userDiagnosticAnswers).length;
  if (totalAnswered < 25) {
    if (!confirm(`You have answered ${totalAnswered} of 25 questions. Would you like to submit now to view your partial diagnostic scorecard?`)) {
      return;
    }
  }

  // Calculate scores per category
  const categoryScores = {
    Communication: { total: 4, correct: 0, name: "Customer Communication & Empathy" },
    Documentation: { total: 4, correct: 0, name: "Ticket Quality & Documentation" },
    ITIL: { total: 4, correct: 0, name: "ITIL Framework & Incident Lifecycle" },
    Troubleshooting: { total: 4, correct: 0, name: "Technical Troubleshooting & Access" },
    Metrics: { total: 4, correct: 0, name: "Metrics, SLAs & XLAs" },
    AI: { total: 5, correct: 0, name: "Responsible AI & Automation" }
  };

  let totalCorrect = 0;

  diagnosticQuestions.forEach(q => {
    const userAns = userDiagnosticAnswers[q.id];
    if (userAns !== undefined && userAns === q.correctIndex) {
      categoryScores[q.category].correct += 1;
      totalCorrect += 1;
    }
  });

  const percentage = Math.round((totalCorrect / 25) * 100);

  // Render Diagnostic Scorecard Modal
  const resultsModal = document.getElementById('diagnostic-results-modal');
  const scoreVal = document.getElementById('diag-score-val');
  const levelRec = document.getElementById('diag-level-rec');
  const breakdownContainer = document.getElementById('diag-breakdown-container');

  if (scoreVal) scoreVal.textContent = `${percentage}% (${totalCorrect}/25 Correct)`;

  let recText = "Level 1: Foundation";
  let recBadgeBg = "bg-emerald-500/20 text-emerald-400 border-emerald-500/30";

  if (percentage >= 85) {
    recText = "Level 4: Lead & Continuous Improvement Practitioner";
    recBadgeBg = "bg-amber-400/20 text-amber-400 border-amber-400/30";
  } else if (percentage >= 65) {
    recText = "Level 3: Advanced ITIL & AI Operations";
    recBadgeBg = "bg-cyberPurple/20 text-cyberPurple border-cyberPurple/30";
  } else if (percentage >= 45) {
    recText = "Level 2: Operational Practitioner";
    recBadgeBg = "bg-cyberBlue/20 text-cyberBlue border-cyberBlue/30";
  }

  if (levelRec) {
    levelRec.className = `px-3 py-1 rounded-full text-xs font-mono font-bold border uppercase inline-block ${recBadgeBg}`;
    levelRec.textContent = `Recommended Starting Point: ${recText}`;
  }

  if (breakdownContainer) {
    breakdownContainer.innerHTML = '';
    Object.keys(categoryScores).forEach(catKey => {
      const cat = categoryScores[catKey];
      const catPct = Math.round((cat.correct / cat.total) * 100);
      let statusColor = "text-emerald-400";
      if (catPct < 50) statusColor = "text-red-400";
      else if (catPct < 75) statusColor = "text-amber-400";

      const catRow = document.createElement('div');
      catRow.className = 'p-3 bg-black/40 border border-slate-800 rounded-xl flex justify-between items-center text-xs font-mono';
      catRow.innerHTML = `
        <div>
          <span class="font-bold text-white block">${cat.name}</span>
          <span class="text-[10px] text-slate-400">${cat.correct} of ${cat.total} Correct</span>
        </div>
        <span class="font-bold ${statusColor}">${catPct}%</span>
      `;
      breakdownContainer.appendChild(catRow);
    });
  }

  if (resultsModal) {
    resultsModal.classList.remove('hidden');
    resultsModal.classList.add('flex');
    setTimeout(() => resultsModal.classList.remove('opacity-0'), 10);
  }
}

function closeDiagnosticResultsModal() {
  const resultsModal = document.getElementById('diagnostic-results-modal');
  if (resultsModal) {
    resultsModal.classList.add('opacity-0');
    setTimeout(() => {
      resultsModal.classList.add('hidden');
      resultsModal.classList.remove('flex');
    }, 300);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  renderDiagnosticQuiz();
});
