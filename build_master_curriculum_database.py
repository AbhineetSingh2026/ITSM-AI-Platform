import json
from pathlib import Path

workspace_dir = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")

# Master Curriculum Database containing all 16 modules across 4 levels
master_curriculum = {
  "courseTitle": "IT Service Desk Operations & AI Triage Masterclass",
  "owner": "Abhineet Singh | AI-ITSM Hub",
  "disclaimer": "Independent, practical, ITIL 4 aligned learning programme. Not affiliated with or endorsed by PeopleCert, Axelos, or ITIL.",
  "levels": [
    {
      "level": 1,
      "levelName": "Level 1: Foundation",
      "targetAudience": "Career starters, beginner analysts, self-service support agents",
      "modules": [
        {
          "id": "mod_1",
          "moduleNum": 1,
          "title": "Service Desk Purpose & Professional Mindset",
          "duration": "45 min",
          "badge": "Helpdesk Basics",
          "desc": "Single Point of Contact (SPOC) role, Helpdesk vs. Service Desk distinction, customer-centric mindset, and ITIL 4 Service Value System foundation.",
          "learningOutcomes": [
            "Explain the SPOC (Single Point of Contact) principle in enterprise IT",
            "Differentiate between Helpdesk, Service Desk, and Enterprise Service Management (ESM)",
            "Apply customer-centric communication during stressful user contacts",
            "Understand the impact of First Contact Resolution (FCR) on business productivity"
          ],
          "keyTakeaways": [
            "Single Point of Contact (SPOC) eliminates user confusion and fragmented IT support.",
            "Service Desk focuses on business value and user experience, not just closed tickets.",
            "Empathy and active listening convert technical frustration into trust.",
            "FCR optimization reduces total cost to resolve and user downtime."
          ],
          "videoScriptTitle": "Module 1: The Modern Service Desk Mindset",
          "videoDuration": "10 min",
          "sopTemplate": "Incident Ticket Quality & SPOC Audit Checklist",
          "quizQuestionsCount": 10,
          "sources": ["PeopleCert ITIL 4 Foundation", "Consortium for Service Innovation KCS"]
        },
        {
          "id": "mod_2",
          "moduleNum": 2,
          "title": "Communication, Empathy & Customer Care",
          "duration": "50 min",
          "badge": "Customer Care",
          "desc": "Active listening techniques, de-escalating anxious users, executive stakeholder communications, and customer satisfaction (CSAT) best practices.",
          "learningOutcomes": [
            "Master de-escalation techniques for anxious or frustrated users",
            "Draft clear, jargon-free resolution communications for non-technical users",
            "Structure executive incident summaries for senior leadership",
            "Implement CSAT feedback loops to improve daily support quality"
          ],
          "keyTakeaways": [
            "De-escalation requires acknowledging emotion before addressing technical root cause.",
            "Jargon-free explanations build user confidence during major disruptions.",
            "Executive summaries require 3 bullets: Business Impact, Action Taken, Next Update Time.",
            "CSAT feedback provides actionable coaching insights for service desk leaders."
          ],
          "videoScriptTitle": "Module 2: Mastering User Communication & De-escalation",
          "videoDuration": "12 min",
          "sopTemplate": "Customer Communication & De-escalation Playbook",
          "quizQuestionsCount": 10,
          "sources": ["ISO/IEC 20000-1", "HDI Support Center Standards"]
        },
        {
          "id": "mod_3",
          "moduleNum": 3,
          "title": "Ticket Lifecycle, Categorisation, Priority & Documentation",
          "duration": "55 min",
          "badge": "Ticket Lifecycle",
          "desc": "Incident vs Request distinction, Priority Matrix (Impact x Urgency calculation), CTI taxonomy tagging, internal work notes, and resolution tagging.",
          "learningOutcomes": [
            "Distinguish between Incidents (disruptions) and Service Requests (routine requests)",
            "Calculate Priority objectively using the Impact x Urgency matrix",
            "Tag Category, Type, and Item (CTI) accurately for automated AI routing",
            "Write audit-proof internal work notes and user-visible comments"
          ],
          "keyTakeaways": [
            "Incidents interrupt business operations; Service Requests ask for predefined access/hardware.",
            "Priority is mathematically derived: Impact (users affected) x Urgency (business deadline).",
            "Accurate CTI tagging enables automated AI triage and problem trend discovery.",
            "Work notes protect compliance and prevent duplicate troubleshooting across teams."
          ],
          "videoScriptTitle": "Module 3: Ticket Lifecycle & Priority Matrix Deep Dive",
          "videoDuration": "15 min",
          "sopTemplate": "Impact x Urgency Priority Assessment Matrix",
          "quizQuestionsCount": 10,
          "sources": ["PeopleCert Incident Management Practice", "ServiceNow ITSM Process Guide"]
        },
        {
          "id": "mod_4",
          "moduleNum": 4,
          "title": "Foundation Troubleshooting & Security Awareness",
          "duration": "50 min",
          "badge": "Security & Basics",
          "desc": "Structured troubleshooting methodology, verifying caller identity, phishing detection, credential protection, and security incident escalation.",
          "learningOutcomes": [
            "Follow the 6-step troubleshooting methodology (Identify, Hypothesize, Test, Plan, Verify, Document)",
            "Verify caller identity securely before performing password resets",
            "Recognize social engineering and phishing attempt patterns",
            "Escalate suspected cybersecurity breaches to the Security Operations Center (SOC)"
          ],
          "keyTakeaways": [
            "Structured troubleshooting prevents random guessing and reduces MTTR.",
            "Identity verification via manager callback or MFA prevents social engineering attacks.",
            "Phishing emails often create artificial urgency and spoof trusted domain names.",
            "Suspected security incidents require immediate SOC isolation and ticket escalation."
          ],
          "videoScriptTitle": "Module 4: Systematic Troubleshooting & Security Hygiene",
          "videoDuration": "11 min",
          "sopTemplate": "Caller Identity Verification & Security Checklist",
          "quizQuestionsCount": 10,
          "sources": ["CISA Phishing Guidance", "UK NCSC Password Policy"]
        }
      ]
    },
    {
      "level": 2,
      "levelName": "Level 2: Operational Practitioner",
      "targetAudience": "Level 1 & Level 2 support analysts, desktop engineers, identity admins",
      "modules": [
        {
          "id": "mod_5",
          "moduleNum": 5,
          "title": "Identity, Access, Active Directory, Entra & Microsoft Support",
          "duration": "60 min",
          "badge": "Active Directory",
          "desc": "Active Directory Domain Services, Microsoft Entra ID (Azure AD), SSPR, MFA token registration, RBAC permissions, and drive mapping.",
          "learningOutcomes": [
            "Manage AD user accounts, OUs, and Security Group memberships",
            "Troubleshoot Microsoft Entra ID (Azure AD) hybrid authentication and SSPR",
            "Register and reset Microsoft Authenticator MFA tokens",
            "Apply Role-Based Access Control (RBAC) to enforce least-privilege security"
          ],
          "keyTakeaways": [
            "Hybrid identity connects local Active Directory to cloud Microsoft Entra ID.",
            "SSPR and automated MFA resets deflect up to 30% of routine helpdesk call volume.",
            "Role-Based Access Control (RBAC) ensures users receive only necessary permissions.",
            "Network drive access issues are usually solved by updating AD Security Groups."
          ],
          "videoScriptTitle": "Module 5: AD & Microsoft Entra Identity Management",
          "videoDuration": "14 min",
          "sopTemplate": "Active Directory & Entra ID Provisioning Guide",
          "quizQuestionsCount": 10,
          "sources": ["Microsoft Learn Entra Identity", "Microsoft Learn SSPR"]
        },
        {
          "id": "mod_6",
          "moduleNum": 6,
          "title": "Windows Endpoint, Application, Printer & Remote Support",
          "duration": "65 min",
          "badge": "Intune & Endpoints",
          "desc": "MS Intune MDM, Autopilot, Windows Event Viewer, application crash dumps, network printer spoolers, and remote assistance tools.",
          "learningOutcomes": [
            "Deploy applications and policies via Microsoft Intune and Company Portal",
            "Analyze Windows Event Logs (System/Application) to isolate software crashes",
            "Clear Windows Print Spooler locks and map network printers",
            "Perform secure remote desktop sessions using MS Quick Assist and TeamViewer"
          ],
          "keyTakeaways": [
            "Microsoft Intune automates cloud endpoint configuration and security wipes.",
            "Event Viewer IDs (e.g. 1000 Application Error) isolate crash root cause instantly.",
            "Print spooler service restarts resolve 80% of stuck network printer queues.",
            "Remote support requires explicit user authorization before taking screen control."
          ],
          "videoScriptTitle": "Module 6: Windows Endpoint & Intune Troubleshooting",
          "videoDuration": "15 min",
          "sopTemplate": "Intune Endpoint & Printer SOP",
          "quizQuestionsCount": 10,
          "sources": ["Microsoft Learn Intune", "Microsoft Sysinternals"]
        },
        {
          "id": "mod_7",
          "moduleNum": 7,
          "title": "Networking, DNS, DHCP, Wi-Fi & VPN Troubleshooting",
          "duration": "60 min",
          "badge": "Networking & VPN",
          "desc": "TCP/IP fundamentals, ipconfig, ping, nslookup, traceroute, DHCP lease renewals, Wi-Fi 802.1X enterprise auth, and GlobalProtect VPN.",
          "learningOutcomes": [
            "Diagnose OSI Layer 1 to Layer 7 network connection failures",
            "Use ping, nslookup, and traceroute to isolate DNS and routing failures",
            "Resolve DHCP IP conflict errors using ipconfig /release and /renew",
            "Troubleshoot GlobalProtect / Cisco AnyConnect VPN gateway timeouts"
          ],
          "keyTakeaways": [
            "Always follow the OSI layer model: Check physical link before software config.",
            "DNS failure (nslookup) is the single most common cause of internal site load failure.",
            "DHCP lease renewal resets stale IP allocations on corporate Wi-Fi networks.",
            "VPN gateway timeouts usually stem from ISP MTU size or MFA expiration."
          ],
          "videoScriptTitle": "Module 7: Network & VPN Diagnostics Masterclass",
          "videoDuration": "13 min",
          "sopTemplate": "Network & VPN Diagnostics SOP",
          "quizQuestionsCount": 10,
          "sources": ["Cisco Networking Academy", "Microsoft TCP/IP Architecture"]
        },
        {
          "id": "mod_8",
          "moduleNum": 8,
          "title": "Service Requests, Approvals, Escalation & Handover",
          "duration": "55 min",
          "badge": "Requests & JML",
          "desc": "Joiners, Movers, Leavers (JML) workflows, hardware provisioning, approval chains, third-party vendor management, and shift handover logs.",
          "learningOutcomes": [
            "Execute automated JML onboarding and offboarding workflows",
            "Manage approval hierarchies for hardware and software procurement",
            "Escalate complex incidents to third-party vendors with SLA tracking",
            "Conduct seamless shift handovers using structured operational logs"
          ],
          "keyTakeaways": [
            "Day 1 Readiness for Joiners requires pre-provisioned hardware and access tokens.",
            "Offboarding (Leavers) requires immediate account lock and remote data wipe for security.",
            "Vendor SLAs must match internal Incident Response targets to prevent contract breaches.",
            "Shift handover logs ensure high-priority P2 incidents are tracked 24/7."
          ],
          "videoScriptTitle": "Module 8: JML Workflows & Vendor Management",
          "videoDuration": "12 min",
          "sopTemplate": "Shift Handover & Operations Log Template",
          "quizQuestionsCount": 10,
          "sources": ["PeopleCert Service Request Management", "ITIL 4 Practice Guides"]
        }
      ]
    },
    {
      "level": 3,
      "levelName": "Level 3: Advanced Analyst",
      "targetAudience": "Senior analysts, Major Incident Managers, KCS Knowledge Managers",
      "modules": [
        {
          "id": "mod_9",
          "moduleNum": 9,
          "title": "Major Incident Support & Stakeholder Communications",
          "duration": "70 min",
          "badge": "P1 Incidents & CAB",
          "desc": "Declaring P1 Major Incidents, establishing bridge calls, executive communications, Emergency CAB approvals, and Post-Incident Reviews (PIR).",
          "learningOutcomes": [
            "Command P1 Major Incident technical war rooms and bridge calls",
            "Publish broadcast status page updates and stakeholder communications",
            "Facilitate Emergency Change Advisory Board (ECAB) risk evaluations",
            "Lead Post-Incident Reviews (PIR) to document timelines and lessons learned"
          ],
          "keyTakeaways": [
            "Major Incident Command requires separating technical resolution from stakeholder comms.",
            "Broadcast updates must be issued every 30 minutes during active P1 outages.",
            "Emergency CAB changes require rapid risk evaluation without skipping security checks.",
            "PIR meetings focus on process improvement, not assigning personal blame."
          ],
          "videoScriptTitle": "Module 9: P1 Major Incident War Room Command",
          "videoDuration": "16 min",
          "sopTemplate": "P1 Major Incident Playbook & Executive Update",
          "quizQuestionsCount": 10,
          "sources": ["PeopleCert Incident Management Practice", "ITIL 4 High-Velocity IT"]
        },
        {
          "id": "mod_10",
          "moduleNum": 10,
          "title": "Problem Management, Known Errors & Root Cause Analysis",
          "duration": "65 min",
          "badge": "Problem Mgt & RCA",
          "desc": "Reactive vs Proactive Problem Management, 5-Why RCA methodology, Fishbone (Ishikawa) diagrams, Known Error Database (KEDB), and workaround publishing.",
          "learningOutcomes": [
            "Differentiate Problem Management from Incident Management",
            "Apply 5-Why Analysis and Fishbone diagrams to isolate root cause",
            "Maintain the Known Error Database (KEDB) with validated workarounds",
            "Calculate business loss to prioritize problem investigation backlogs"
          ],
          "keyTakeaways": [
            "Problem Management eliminates recurring incidents to protect long-term business productivity.",
            "5-Why analysis drills down past surface symptoms to underlying process or system failures.",
            "KEDB workarounds allow L1 analysts to restore service while permanent fixes build.",
            "Proactive Problem Management analyzes ticket trends to fix flaws before outages occur."
          ],
          "videoScriptTitle": "Module 10: 5-Why RCA & Problem Management",
          "videoDuration": "14 min",
          "sopTemplate": "5-Why Root Cause Analysis (RCA) Worksheet",
          "quizQuestionsCount": 10,
          "sources": ["PeopleCert Problem Management Practice", "Lean Six Sigma RCA Guide"]
        },
        {
          "id": "mod_11",
          "moduleNum": 11,
          "title": "KCS, Knowledge Quality & Analyst Coaching",
          "duration": "60 min",
          "badge": "KCS & Knowledge",
          "desc": "Knowledge-Centered Service (KCS v6) methodology, Solve Loop (Capture, Structure, Reuse, Improve), Evolve Loop, article quality index (AQI), and coaching.",
          "learningOutcomes": [
            "Apply KCS Solve Loop mechanics during active ticket resolution",
            "Structure Knowledge Base (KB) articles using standard problem/solution templates",
            "Evaluate Knowledge Quality using the Article Quality Index (AQI)",
            "Coach L1/L2 analysts to adopt knowledge creation as a daily habit"
          ],
          "keyTakeaways": [
            "KCS integrates knowledge creation directly into the ticket resolution workflow.",
            "Capture in the workflow: Write articles in the user's language while solving the ticket.",
            "Reuse and improve: Search first, modify existing articles before creating duplicates.",
            "AQI audits maintain KB health and prevent outdated or unverified guides."
          ],
          "videoScriptTitle": "Module 11: KCS Methodology & Knowledge Engineering",
          "videoDuration": "13 min",
          "sopTemplate": "KCS Knowledge Article Drafting Template",
          "quizQuestionsCount": 10,
          "sources": ["Consortium for Service Innovation KCS v6", "ITIL 4 Knowledge Management"]
        },
        {
          "id": "mod_12",
          "moduleNum": 12,
          "title": "Automation, Operational Data & Responsible AI Assistance",
          "duration": "75 min",
          "badge": "AI & Automation",
          "desc": "Zero-touch ticket triage, LLM intent classification, Retrieval-Augmented Generation (RAG) virtual agents, prompt engineering, and NCSC/OWASP AI safety.",
          "learningOutcomes": [
            "Build zero-touch AI triage workflows for L1 password and access requests",
            "Implement Retrieval-Augmented Generation (RAG) to ground AI responses in approved KBs",
            "Apply NCSC and OWASP security guidelines to prevent prompt injection and data leaks",
            "Maintain Human-in-the-Loop (HITL) oversight for high-risk automated actions"
          ],
          "keyTakeaways": [
            "AI Virtual Agents deflect up to 40% of L1 tickets when grounded in reliable KBs.",
            "RAG architecture prevents AI hallucinations by forcing responses to cite official SOPs.",
            "Never input real passwords, PII, or patient data into public AI prompts.",
            "Human-in-the-Loop (HITL) validation is mandatory for administrative access modifications."
          ],
          "videoScriptTitle": "Module 12: Next-Gen AI Service Desk & RAG Architecture",
          "videoDuration": "18 min",
          "sopTemplate": "Responsible AI Triage & Prompt Security Guide",
          "quizQuestionsCount": 10,
          "sources": ["NIST AI Risk Management Framework", "OWASP Top 10 for LLM Applications", "UK NCSC Secure AI Guidance"]
        }
      ]
    },
    {
      "level": 4,
      "levelName": "Level 4: Lead & Improvement Practitioner",
      "targetAudience": "Service Desk Managers, IT Operations Leaders, Service Delivery Managers",
      "modules": [
        {
          "id": "mod_13",
          "moduleNum": 13,
          "title": "Service Desk Operating Model, Demand & Workforce",
          "duration": "80 min",
          "badge": "Leadership & Ops",
          "desc": "Service Desk operating models (Centralized, Distributed, Virtual, Follow-the-Sun), Erlang-C capacity planning, shift roster optimization, and talent retention.",
          "learningOutcomes": [
            "Design optimal Service Desk operating models for global enterprise support",
            "Apply Erlang-C calculations to predict phone staffing requirements during peak hours",
            "Structure shift rosters to prevent analyst burnout and maintain SLA coverage",
            "Build career pathways to retain talent and promote analysts from L1 -> L2 -> Management"
          ],
          "keyTakeaways": [
            "Operating models (Virtual vs Follow-the-Sun) must balance cost, language, and timezone needs.",
            "Erlang-C algorithms model call queue arrival rates to determine minimum required staffing.",
            "Over-staffing wastes budget; under-staffing causes call abandonment and SLA breach.",
            "Clear promotion pathways increase team retention and institutional knowledge."
          ],
          "videoScriptTitle": "Module 13: Operating Models & Workforce Capacity Planning",
          "videoDuration": "18 min",
          "sopTemplate": "Workforce Capacity & Roster Planning Template",
          "quizQuestionsCount": 10,
          "sources": ["HDI Service Desk Leadership Standards", "ITIL 4 Service Financial Management"]
        },
        {
          "id": "mod_14",
          "moduleNum": 14,
          "title": "Metrics, SLA, XLA & Service-Review Reporting",
          "duration": "75 min",
          "badge": "XLAs & Scorecards",
          "desc": "Transitioning from SLAs to XLAs (Experience Level Agreements), sentiment analysis, executive dashboard design, watermelon index mitigation, and SLA data dictionaries.",
          "learningOutcomes": [
            "Eliminate the 'Watermelon Effect' (Green SLAs, Red User Sentiment)",
            "Design Employee Experience Level Agreements (XLAs) measuring ease of use and sentiment",
            "Construct executive scorecards tracking FCR, MTTR, CSAT, and Cost Per Contact",
            "Facilitate monthly Business Service Review meetings with executive stakeholders"
          ],
          "keyTakeaways": [
            "Traditional SLAs measure system uptime; XLAs measure end-user productivity and happiness.",
            "The Watermelon Index indicates severe operational failure hidden behind green SLA metrics.",
            "Analyst Scorecards should weigh quality (CSAT/AQI) higher than pure closed ticket count.",
            "Service Reviews focus on business outcomes and continuous value delivery."
          ],
          "videoScriptTitle": "Module 14: Designing XLAs & Executive Scorecards",
          "videoDuration": "16 min",
          "sopTemplate": "XLA Governance & Executive Reporting Playbook",
          "quizQuestionsCount": 10,
          "sources": ["HappySignals Experience Management", "ITIL 4 Continual Improvement"]
        },
        {
          "id": "mod_15",
          "moduleNum": 15,
          "title": "Quality Assurance, Coaching & Continual Improvement",
          "duration": "70 min",
          "badge": "QA & Improvement",
          "desc": "Quality Assurance (QA) audit frameworks, 1-on-1 analyst coaching, Continual Improvement Register (CIR), Benchmarking, and Deming Cycle (PDCA).",
          "learningOutcomes": [
            "Implement weekly QA ticket and call auditing programs",
            "Conduct constructive 1-on-1 coaching sessions using the GROW model",
            "Maintain the Continual Improvement Register (CIR) to prioritize efficiency projects",
            "Apply Plan-Do-Check-Act (PDCA) to drive measurable annual cost savings"
          ],
          "keyTakeaways": [
            "QA programs audit call recordings and ticket work notes for technical and soft skills.",
            "Coaching sessions should be collaborative, focusing on growth rather than punitive measures.",
            "The Continual Improvement Register (CIR) tracks all small and large improvement ideas.",
            "PDCA ensures improvements are validated empirically before scaling across the organization."
          ],
          "videoScriptTitle": "Module 15: QA Auditing & Continual Improvement (CSI)",
          "videoDuration": "15 min",
          "sopTemplate": "Continual Improvement Register (CIR) Worksheet",
          "quizQuestionsCount": 10,
          "sources": ["PeopleCert Continual Improvement Practice", "Deming Cycle Framework"]
        },
        {
          "id": "mod_16",
          "moduleNum": 16,
          "title": "AI Governance, Risk Management & Transformation Capstone",
          "duration": "90 min",
          "badge": "Capstone & Governance",
          "desc": "AI risk registers, ISO 42001 AI Management System, ROI calculation for ITSM tooling, and the Grand Master 90-Day Service Desk Transformation Capstone.",
          "learningOutcomes": [
            "Develop AI Risk Registers aligned with ISO 42001 and NIST AI Risk Management Framework",
            "Calculate Return on Investment (ROI) for ITSM platform migrations (e.g. ServiceNow to Halo ESM)",
            "Formulate a comprehensive 90-Day IT Service Desk Transformation Roadmap",
            "Complete the Grand Master 50-Question Final Capstone Examination"
          ],
          "keyTakeaways": [
            "AI Governance mandates logging prompt data, securing API integrations, and auditing model drift.",
            "Tooling migrations require calculating Total Cost of Ownership (TCO) including licenses and implementation.",
            "A successful 90-day roadmap balances quick wins (password deflection) with strategic changes (KCS/XLAs).",
            "The Grand Master Capstone validates end-to-end operational mastery across Level 1–4 curriculum."
          ],
          "videoScriptTitle": "Module 16: AI Governance & 90-Day Transformation Capstone",
          "videoDuration": "20 min",
          "sopTemplate": "90-Day Service Desk Transformation Roadmap Template",
          "quizQuestionsCount": 10,
          "sources": ["ISO/IEC 42001 AI Management Standard", "NIST AI RMF 1.0", "ICO AI Guidance"]
        }
      ]
    }
  ]
}

# Save Master Curriculum Database JSON
json_path = workspace_dir / "course_curriculum_master.json"
json_path.write_text(json.dumps(master_curriculum, indent=2), encoding="utf-8")
print(f"[OK] Saved Master Curriculum Database to {json_path}")
