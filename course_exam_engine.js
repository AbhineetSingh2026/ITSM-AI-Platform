
// -------------------------------------------------------------------
// IT SERVICE DESK & AI OPERATIONS ACADEMY — AUTOMATED EXAM ENGINE
// -------------------------------------------------------------------

const EXAM_DATABASE = {
  "level1": [
    {
      "id": "l1_q1",
      "level": 1,
      "chapter": 1,
      "question": "An end-user calls stating their laptop won't power on. What is the very first step the L1 analyst should perform according to Service Desk best practices?",
      "options": [
        "Log a ticket, request an immediate motherboard replacement, and dispatch an engineer.",
        "Verify caller identity, actively listen to the issue details, and ask basic power connectivity questions.",
        "Escalate immediately to the L3 Infrastructure Systems engineering team.",
        "Tell the user to buy a new charger without logging a ticket."
      ],
      "answer": 1,
      "explanation": "L1 analysts must first verify user identity, actively listen to clarify symptoms, and troubleshoot basic physical connectivity before escalating."
    },
    {
      "id": "l1_q2",
      "level": 1,
      "chapter": 1,
      "question": "What is the primary definition of First Contact Resolution (FCR)?",
      "options": [
        "Resolving the issue during the initial call/chat interaction without escalating or re-contacting.",
        "Resolving a ticket within 24 hours regardless of how many teams worked on it.",
        "Closing a ticket automatically when no update is received from the user.",
        "Assigning the ticket to the vendor within 15 minutes."
      ],
      "answer": 0,
      "explanation": "FCR measures tickets successfully resolved during the initial contact with the Service Desk without needing multi-tier escalation."
    },
    {
      "id": "l1_q3",
      "level": 1,
      "chapter": 2,
      "question": "How is ticket Priority calculated in standard ITSM frameworks?",
      "options": [
        "Based solely on the VIP status of the caller.",
        "Priority = Impact (business blast radius) \u00d7 Urgency (time sensitivity).",
        "Priority = Analyst workload \u00d7 Department budget.",
        "Randomly assigned by the ticketing system queue."
      ],
      "answer": 1,
      "explanation": "ITIL calculates Priority as a combination of Impact (how many users/services affected) and Urgency (how quickly the business requires a fix)."
    },
    {
      "id": "l1_q4",
      "level": 1,
      "chapter": 2,
      "question": "A single user cannot print to their local office printer. How should this issue be classified?",
      "options": [
        "P1 Critical Incident (Major Outage)",
        "P2 High Incident",
        "P4 Low / Standard Incident",
        "Service Request for Change"
      ],
      "answer": 2,
      "explanation": "Single-user non-critical localized issues have low business impact and are categorized as P4 Low."
    },
    {
      "id": "l1_q5",
      "level": 1,
      "chapter": 3,
      "question": "A user gets an 'Account Locked Out' error in Active Directory after entering their password wrong multiple times. What is the correct remediation?",
      "options": [
        "Delete the Active Directory account and recreate it.",
        "Verify identity via secondary MFA/manager verification, unlock the account in AD, and reset the password if needed.",
        "Format the user's hard drive.",
        "Ask the user to wait 72 hours for self-healing."
      ],
      "answer": 1,
      "explanation": "Account lockouts in Active Directory require identity verification followed by unlocking the account object in AD Users & Computers."
    },
    {
      "id": "l1_q6",
      "level": 1,
      "chapter": 3,
      "question": "What Active Directory object container is used to organize users, computers, and groups hierarchically?",
      "options": [
        "Organizational Unit (OU)",
        "Domain Name System (DNS)",
        "Dynamic Host Configuration Protocol (DHCP)",
        "Group Policy Object (GPO)"
      ],
      "answer": 0,
      "explanation": "Organizational Units (OUs) are containers within AD domains used to structure and manage objects and apply Group Policies."
    },
    {
      "id": "l1_q7",
      "level": 1,
      "chapter": 4,
      "question": "What is the main difference between SLA Response Time and SLA Resolution Time?",
      "options": [
        "Response Time is when the analyst first acknowledges/touches the ticket; Resolution Time is when the issue is fixed.",
        "Response Time is for phone calls only; Resolution Time is for emails only.",
        "They are identical metrics with different names.",
        "Response Time is measured in days; Resolution Time is measured in minutes."
      ],
      "answer": 0,
      "explanation": "SLA Response Time tracks initial acknowledgement/assignment, while Resolution Time tracks complete ticket resolution."
    },
    {
      "id": "l1_q8",
      "level": 1,
      "chapter": 1,
      "question": "Which field in a Service Desk ticket records detailed technical steps taken during troubleshooting for audit and peer review?",
      "options": [
        "Category Dropdown",
        "Work Notes / Activity Log",
        "Short Description Header",
        "Caller Telephone Number"
      ],
      "answer": 1,
      "explanation": "Work Notes / Activity Log stores internal technical investigation notes, diagnostic outputs, and steps taken by analysts."
    },
    {
      "id": "l1_q9",
      "level": 1,
      "chapter": 2,
      "question": "What is the difference between an Incident and a Service Request?",
      "options": [
        "An Incident is an unplanned interruption/degradation of service; a Service Request is a formal user request for something to be provided (e.g. software access).",
        "An Incident is raised by IT; a Service Request is raised by external vendors.",
        "An Incident never has an SLA; a Service Request always has a 5-minute SLA.",
        "There is no difference in modern ITIL v4."
      ],
      "answer": 0,
      "explanation": "ITIL defines Incidents as service disruptions requiring restoration, whereas Service Requests are standard fulfillments like new access or hardware."
    },
    {
      "id": "l1_q10",
      "level": 1,
      "chapter": 3,
      "question": "Which protocol is commonly used for secure multi-factor authentication (MFA) push notifications on mobile devices?",
      "options": [
        "OAuth 2.0 / TOTP Push (e.g. Microsoft Authenticator)",
        "POP3 Email protocol",
        "FTP File Transfer",
        "Telnet clear text"
      ],
      "answer": 0,
      "explanation": "Modern MFA relies on secure OAuth 2.0 push tokens and Time-based One-Time Password (TOTP) protocols."
    },
    {
      "id": "l1_q11",
      "level": 1,
      "chapter": 4,
      "question": "When an analyst must place a caller on hold to consult L2, what is the professional etiquette?",
      "options": [
        "Mute the line instantly without saying anything.",
        "Ask permission, state the reason, provide an estimated wait time (e.g., 2 minutes), and thank them upon return.",
        "Disconnect the call and email the answer later.",
        "Transfer the call blindly to a random extension."
      ],
      "answer": 1,
      "explanation": "Professional call handling requires asking permission, setting expectations for hold duration, and thanking the user when resuming."
    },
    {
      "id": "l1_q12",
      "level": 1,
      "chapter": 2,
      "question": "A user's Outlook crashes continuously whenever an email with a large PDF is opened. What state should the ticket be set to while waiting for the user to reply with sample files?",
      "options": [
        "Resolved",
        "On Hold / Pending Customer",
        "Closed",
        "Cancelled"
      ],
      "answer": 1,
      "explanation": "When awaiting necessary information or action from the end-user, tickets are placed in 'On Hold - Pending Customer' to pause the SLA clock."
    },
    {
      "id": "l1_q13",
      "level": 1,
      "chapter": 3,
      "question": "What is the security risk of sharing administrative domain credentials across Service Desk analysts?",
      "options": [
        "It speeds up ticket resolution.",
        "It breaks accountability, prevents non-repudiation, and violates security compliance frameworks.",
        "It reduces server CPU usage.",
        "It automatically updates Windows OS."
      ],
      "answer": 1,
      "explanation": "Shared admin credentials prevent auditing who performed specific administrative actions, violating ISO 27001 and Cyber Essentials compliance."
    },
    {
      "id": "l1_q14",
      "level": 1,
      "chapter": 4,
      "question": "What is CSAT?",
      "options": [
        "Customer Satisfaction score collected through post-resolution surveys.",
        "Computer System Automated Testing tool.",
        "Cyber Security Alarm Trigger.",
        "Central Server Application Token."
      ],
      "answer": 0,
      "explanation": "CSAT (Customer Satisfaction) measures end-user satisfaction with the service provided by the Service Desk analyst."
    },
    {
      "id": "l1_q15",
      "level": 1,
      "chapter": 1,
      "question": "What is the main goal of Shift-Left in L1 Helpdesk support?",
      "options": [
        "Moving complex troubleshooting knowledge down to L1 and self-service to resolve issues faster at lower cost.",
        "Moving all tickets to external third-party call centers.",
        "Deleting old tickets from the database.",
        "Ignoring low-priority tickets."
      ],
      "answer": 0,
      "explanation": "Shift-Left empowers lower tiers (L1 and end-user self-service AI) to handle tasks previously restricted to L2/L3 engineers."
    },
    {
      "id": "l1_q16",
      "level": 1,
      "chapter": 2,
      "question": "Which of the following is a key requirement before closing a ticket?",
      "options": [
        "Adding a clear Resolution Summary and confirming user satisfaction.",
        "Deleting the user's phone number.",
        "Escalating to executive management.",
        "Changing the caller's job title."
      ],
      "answer": 0,
      "explanation": "Proper ticket closure requires documenting the root resolution steps and verifying the user's issue is resolved."
    },
    {
      "id": "l1_q17",
      "level": 1,
      "chapter": 3,
      "question": "What command line tool checks local IP address configuration on a Windows workstation?",
      "options": [
        "ipconfig /all",
        "ping google.com",
        "traceroute",
        "chkdsk C:"
      ],
      "answer": 0,
      "explanation": "ipconfig /all displays detailed network interface information including IP, Subnet Mask, Gateway, and DNS servers."
    },
    {
      "id": "l1_q18",
      "level": 1,
      "chapter": 4,
      "question": "Why is active listening crucial when taking a support ticket call?",
      "options": [
        "It ensures all technical and emotional nuances are understood, reducing misdiagnosis.",
        "It allows the analyst to finish typing faster.",
        "It automatically logs the caller into ServiceNow.",
        "It bypasses security verification."
      ],
      "answer": 0,
      "explanation": "Active listening ensures analysts capture exact error messages, business impact, and user concerns accurately."
    },
    {
      "id": "l1_q19",
      "level": 1,
      "chapter": 2,
      "question": "What is a 'Workaround' in ITIL Incident Management?",
      "options": [
        "A temporary solution that restores service availability while permanent root cause analysis is conducted.",
        "An illegal modification to code.",
        "A permanent hardware upgrade.",
        "An automated email auto-responder."
      ],
      "answer": 0,
      "explanation": "A workaround is a temporary fix deployed to restore business continuity quickly while a permanent fix is researched."
    },
    {
      "id": "l1_q20",
      "level": 1,
      "chapter": 3,
      "question": "What does MFA stand for in endpoint identity security?",
      "options": [
        "Multi-Factor Authentication",
        "Main Firewall Architecture",
        "Microsoft File Access",
        "Master Function Agent"
      ],
      "answer": 0,
      "explanation": "MFA (Multi-Factor Authentication) requires users to provide two or more verification factors to gain access."
    }
  ],
  "level2": [
    {
      "id": "l2_q1",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q1] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q2",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q2] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q3",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q3] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q4",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q4] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q5",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q5] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q6",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q6] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q7",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q7] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q8",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q8] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q9",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q9] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q10",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q10] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q11",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q11] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q12",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q12] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q13",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q13] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q14",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q14] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q15",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q15] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q16",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q16] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q17",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q17] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q18",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q18] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q19",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q19] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q20",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q20] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q21",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q21] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q22",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q22] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q23",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q23] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q24",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q24] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q25",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q25] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q26",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q26] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q27",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q27] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q28",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q28] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q29",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q29] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q30",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q30] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    }
  ],
  "level3": [
    {
      "id": "l3_q1",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q1] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q2",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q2] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q3",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q3] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q4",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q4] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q5",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q5] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q6",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q6] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q7",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q7] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q8",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q8] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q9",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q9] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q10",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q10] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q11",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q11] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q12",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q12] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q13",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q13] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q14",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q14] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q15",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q15] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q16",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q16] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q17",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q17] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q18",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q18] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q19",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q19] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q20",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q20] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q21",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q21] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q22",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q22] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q23",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q23] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q24",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q24] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q25",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q25] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q26",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q26] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q27",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q27] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q28",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q28] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q29",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q29] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q30",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q30] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q31",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q31] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q32",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q32] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q33",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q33] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q34",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q34] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q35",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q35] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q36",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q36] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q37",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q37] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q38",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q38] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q39",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q39] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q40",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q40] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    }
  ],
  "final": [
    {
      "id": "l1_q1",
      "level": 1,
      "chapter": 1,
      "question": "An end-user calls stating their laptop won't power on. What is the very first step the L1 analyst should perform according to Service Desk best practices?",
      "options": [
        "Log a ticket, request an immediate motherboard replacement, and dispatch an engineer.",
        "Verify caller identity, actively listen to the issue details, and ask basic power connectivity questions.",
        "Escalate immediately to the L3 Infrastructure Systems engineering team.",
        "Tell the user to buy a new charger without logging a ticket."
      ],
      "answer": 1,
      "explanation": "L1 analysts must first verify user identity, actively listen to clarify symptoms, and troubleshoot basic physical connectivity before escalating."
    },
    {
      "id": "l1_q2",
      "level": 1,
      "chapter": 1,
      "question": "What is the primary definition of First Contact Resolution (FCR)?",
      "options": [
        "Resolving the issue during the initial call/chat interaction without escalating or re-contacting.",
        "Resolving a ticket within 24 hours regardless of how many teams worked on it.",
        "Closing a ticket automatically when no update is received from the user.",
        "Assigning the ticket to the vendor within 15 minutes."
      ],
      "answer": 0,
      "explanation": "FCR measures tickets successfully resolved during the initial contact with the Service Desk without needing multi-tier escalation."
    },
    {
      "id": "l1_q3",
      "level": 1,
      "chapter": 2,
      "question": "How is ticket Priority calculated in standard ITSM frameworks?",
      "options": [
        "Based solely on the VIP status of the caller.",
        "Priority = Impact (business blast radius) \u00d7 Urgency (time sensitivity).",
        "Priority = Analyst workload \u00d7 Department budget.",
        "Randomly assigned by the ticketing system queue."
      ],
      "answer": 1,
      "explanation": "ITIL calculates Priority as a combination of Impact (how many users/services affected) and Urgency (how quickly the business requires a fix)."
    },
    {
      "id": "l1_q4",
      "level": 1,
      "chapter": 2,
      "question": "A single user cannot print to their local office printer. How should this issue be classified?",
      "options": [
        "P1 Critical Incident (Major Outage)",
        "P2 High Incident",
        "P4 Low / Standard Incident",
        "Service Request for Change"
      ],
      "answer": 2,
      "explanation": "Single-user non-critical localized issues have low business impact and are categorized as P4 Low."
    },
    {
      "id": "l1_q5",
      "level": 1,
      "chapter": 3,
      "question": "A user gets an 'Account Locked Out' error in Active Directory after entering their password wrong multiple times. What is the correct remediation?",
      "options": [
        "Delete the Active Directory account and recreate it.",
        "Verify identity via secondary MFA/manager verification, unlock the account in AD, and reset the password if needed.",
        "Format the user's hard drive.",
        "Ask the user to wait 72 hours for self-healing."
      ],
      "answer": 1,
      "explanation": "Account lockouts in Active Directory require identity verification followed by unlocking the account object in AD Users & Computers."
    },
    {
      "id": "l1_q6",
      "level": 1,
      "chapter": 3,
      "question": "What Active Directory object container is used to organize users, computers, and groups hierarchically?",
      "options": [
        "Organizational Unit (OU)",
        "Domain Name System (DNS)",
        "Dynamic Host Configuration Protocol (DHCP)",
        "Group Policy Object (GPO)"
      ],
      "answer": 0,
      "explanation": "Organizational Units (OUs) are containers within AD domains used to structure and manage objects and apply Group Policies."
    },
    {
      "id": "l1_q7",
      "level": 1,
      "chapter": 4,
      "question": "What is the main difference between SLA Response Time and SLA Resolution Time?",
      "options": [
        "Response Time is when the analyst first acknowledges/touches the ticket; Resolution Time is when the issue is fixed.",
        "Response Time is for phone calls only; Resolution Time is for emails only.",
        "They are identical metrics with different names.",
        "Response Time is measured in days; Resolution Time is measured in minutes."
      ],
      "answer": 0,
      "explanation": "SLA Response Time tracks initial acknowledgement/assignment, while Resolution Time tracks complete ticket resolution."
    },
    {
      "id": "l1_q8",
      "level": 1,
      "chapter": 1,
      "question": "Which field in a Service Desk ticket records detailed technical steps taken during troubleshooting for audit and peer review?",
      "options": [
        "Category Dropdown",
        "Work Notes / Activity Log",
        "Short Description Header",
        "Caller Telephone Number"
      ],
      "answer": 1,
      "explanation": "Work Notes / Activity Log stores internal technical investigation notes, diagnostic outputs, and steps taken by analysts."
    },
    {
      "id": "l1_q9",
      "level": 1,
      "chapter": 2,
      "question": "What is the difference between an Incident and a Service Request?",
      "options": [
        "An Incident is an unplanned interruption/degradation of service; a Service Request is a formal user request for something to be provided (e.g. software access).",
        "An Incident is raised by IT; a Service Request is raised by external vendors.",
        "An Incident never has an SLA; a Service Request always has a 5-minute SLA.",
        "There is no difference in modern ITIL v4."
      ],
      "answer": 0,
      "explanation": "ITIL defines Incidents as service disruptions requiring restoration, whereas Service Requests are standard fulfillments like new access or hardware."
    },
    {
      "id": "l1_q10",
      "level": 1,
      "chapter": 3,
      "question": "Which protocol is commonly used for secure multi-factor authentication (MFA) push notifications on mobile devices?",
      "options": [
        "OAuth 2.0 / TOTP Push (e.g. Microsoft Authenticator)",
        "POP3 Email protocol",
        "FTP File Transfer",
        "Telnet clear text"
      ],
      "answer": 0,
      "explanation": "Modern MFA relies on secure OAuth 2.0 push tokens and Time-based One-Time Password (TOTP) protocols."
    },
    {
      "id": "l2_q1",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q1] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q2",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q2] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q3",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q3] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q4",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q4] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q5",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q5] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q6",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q6] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q7",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q7] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q8",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q8] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q9",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q9] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q10",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q10] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q11",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q11] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q12",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q12] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q13",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q13] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q14",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q14] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q15",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q15] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q16",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q16] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l2_q17",
      "level": 2,
      "chapter": 5,
      "question": "[Level 2 - Q17] A user's Intune-managed laptop is reported stolen. What immediate Intune action should be taken from the Microsoft Endpoint Manager admin center?",
      "options": [
        "Initiate a Remote Wipe / Lock command on the device.",
        "Reinstall Windows 11 manually.",
        "Delete the Active Directory user account.",
        "Send an email to the thief."
      ],
      "answer": 0,
      "explanation": "Intune allows security administrators to trigger an immediate Remote Wipe or Lock command to protect enterprise data on stolen endpoints."
    },
    {
      "id": "l2_q18",
      "level": 2,
      "chapter": 6,
      "question": "[Level 2 - Q18] A clinician cannot log into EMIS Web / SystmOne due to a 'Database Connection Failed' error on their workstation. What should L2 check first?",
      "options": [
        "Local network connectivity, VPN status, and EMIS client config files before restarting the client service.",
        "Format the server.",
        "Order a new printer.",
        "Ask the clinician to change their home WiFi password."
      ],
      "answer": 0,
      "explanation": "Clinical app connectivity failures require verifying network/VPN paths, client database config files, and service states."
    },
    {
      "id": "l2_q19",
      "level": 2,
      "chapter": 7,
      "question": "[Level 2 - Q19] In an automated JML (Joiner Mover Leaver) workflow, what is the best practice for a Leaver's mailbox and data retention?",
      "options": [
        "Convert mailbox to Shared Mailbox, assign access to manager, preserve OneDrive data according to policy, and revoke active tokens.",
        "Delete all emails instantly without backup.",
        "Post the password publicly on Teams.",
        "Keep the user logged in forever."
      ],
      "answer": 0,
      "explanation": "Leaver governance dictates converting mailboxes to shared access, retaining data per retention policies, and revoking authentication tokens."
    },
    {
      "id": "l2_q20",
      "level": 2,
      "chapter": 8,
      "question": "[Level 2 - Q20] During a Major Incident (P1 Outage), what is the primary role of the Major Incident Manager on the incident bridge?",
      "options": [
        "Lead technical bridge coordination, drive rapid restoration, maintain executive updates, and manage communications.",
        "Write code fixes live on production database.",
        "Answer L1 password reset phone calls.",
        "Close all open tickets in the backlog."
      ],
      "answer": 0,
      "explanation": "Major Incident Managers lead technical coordination bridges, direct resource allocation, and manage stakeholder communication."
    },
    {
      "id": "l3_q1",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q1] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q2",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q2] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q3",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q3] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q4",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q4] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q5",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q5] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q6",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q6] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q7",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q7] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q8",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q8] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q9",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q9] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q10",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q10] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q11",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q11] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q12",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q12] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q13",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q13] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q14",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q14] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q15",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q15] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q16",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q16] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    },
    {
      "id": "l3_q17",
      "level": 3,
      "chapter": 9,
      "question": "[Level 3 - Q17] According to KCS (Knowledge-Centered Service) principles, when should Knowledge Base articles be created or updated?",
      "options": [
        "In the workflow by analysts at the point of ticket resolution.",
        "Once a year by external consultants.",
        "Only after a major system failure occurs.",
        "By senior management during annual reviews."
      ],
      "answer": 0,
      "explanation": "KCS dictates that knowledge is captured, refined, and published continuously in the workflow by analysts resolving issues."
    },
    {
      "id": "l3_q18",
      "level": 3,
      "chapter": 10,
      "question": "[Level 3 - Q18] Why are Experience Level Agreements (XLAs) replacing traditional SLAs in modern enterprise IT Service Management?",
      "options": [
        "SLAs measure technical availability (e.g. 99.9% uptime) but miss end-user frustration; XLAs measure true user sentiment & productivity.",
        "XLAs are cheaper to buy than SLAs.",
        "SLAs are illegal under GDPR.",
        "XLAs eliminate the need for IT managers."
      ],
      "answer": 0,
      "explanation": "XLAs focus on employee experience, ease of use, and sentiment rather than purely technical SLA availability timers."
    },
    {
      "id": "l3_q19",
      "level": 3,
      "chapter": 11,
      "question": "[Level 3 - Q19] How does Halo ESM or ServiceNow facilitate Enterprise Service Management (ESM) expansion beyond IT?",
      "options": [
        "By providing pre-built request portals, asset catalogs, and workflows for HR, Facilities, and Finance on one unified platform.",
        "By replacing all company laptop hardware automatically.",
        "By sending automated spam text messages to customers.",
        "By deleting non-IT departments."
      ],
      "answer": 0,
      "explanation": "ESM applies ITIL service catalog and ticket routing principles across HR, Facilities, Legal, and Finance departments."
    },
    {
      "id": "l3_q20",
      "level": 3,
      "chapter": 12,
      "question": "[Level 3 - Q20] In an AI-powered IT Service Desk architecture, what is the role of Natural Language Intent Classification?",
      "options": [
        "Analyzing user ticket descriptions to categorize issues, extract entities, and trigger zero-touch resolution workflows.",
        "Translating text into ancient languages.",
        "Generating random ticket numbers.",
        "Compressing database log files."
      ],
      "answer": 0,
      "explanation": "Intent classification models categorize user text, detect urgency, and route or auto-resolve tickets without human intervention."
    }
  ]
};

let currentExamState = {
    examType: null, // 'level1', 'level2', 'level3', 'final'
    examTitle: '',
    questions: [],
    currentIndex: 0,
    userAnswers: {},
    startTime: null,
    totalTimeSeconds: 0,
    timerInterval: null,
    passingScorePct: 70
};

function launchExam(type) {
    let title = "";
    let qs = [];
    let passPct = 70;

    if (type === 'level1') {
        title = "Level 1: Foundation Certification Exam (20 Questions)";
        qs = EXAM_DATABASE.level1;
    } else if (type === 'level2') {
        title = "Level 2: Intermediate Certification Exam (30 Questions)";
        qs = EXAM_DATABASE.level2;
    } else if (type === 'level3') {
        title = "Level 3: Advanced ITIL & AI Operations Exam (40 Questions)";
        qs = EXAM_DATABASE.level3;
    } else if (type === 'final') {
        title = "🏆 Grand Master Certification Exam (50 Questions | 100 Marks)";
        qs = EXAM_DATABASE.final;
    }

    currentExamState.examType = type;
    currentExamState.examTitle = title;
    currentExamState.questions = JSON.parse(JSON.stringify(qs));
    currentExamState.currentIndex = 0;
    currentExamState.userAnswers = {};
    currentExamState.startTime = new Date();
    currentExamState.totalTimeSeconds = 0;
    currentExamState.passingScorePct = passPct;

    if (currentExamState.timerInterval) clearInterval(currentExamState.timerInterval);
    currentExamState.timerInterval = setInterval(() => {
        currentExamState.totalTimeSeconds++;
        updateExamTimerDisplay();
    }, 1000);

    renderExamModal();
}

function updateExamTimerDisplay() {
    const timerElem = document.getElementById('examTimerDisplay');
    if (!timerElem) return;
    const mins = Math.floor(currentExamState.totalTimeSeconds / 60);
    const secs = currentExamState.totalTimeSeconds % 60;
    timerElem.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

function renderExamModal() {
    let modal = document.getElementById('examRunnerModalOverlay');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'examRunnerModalOverlay';
        modal.className = 'modal-overlay';
        document.body.appendChild(modal);
    }

    const q = currentExamState.questions[currentExamState.currentIndex];
    const totalQ = currentExamState.questions.length;
    const selectedAns = currentExamState.userAnswers[currentExamState.currentIndex];

    let optionsHtml = '';
    q.options.forEach((optText, optIdx) => {
        const isChecked = (selectedAns === optIdx) ? 'checked' : '';
        const activeClass = (selectedAns === optIdx) ? 'selected-option' : '';
        optionsHtml += `
            <div class="exam-option-card ${activeClass}" onclick="selectExamOption(${optIdx})">
                <input type="radio" name="examOpt" value="${optIdx}" ${isChecked} style="margin-right: 0.75rem; accent-color: #7c3aed;">
                <label style="cursor: pointer; font-size: 0.95rem; font-weight: 600; color: var(--text-main); flex: 1;">${optText}</label>
            </div>
        `;
    });

    const progressPct = Math.round(((currentExamState.currentIndex + 1) / totalQ) * 100);

    modal.innerHTML = `
        <div class="contact-modal" style="max-width: 800px; height: 90vh; max-height: 750px; display: flex; flex-direction: column;">
            <div class="modal-header" style="background: linear-gradient(135deg, #005eb8, #7c3aed); color: white;">
                <div class="modal-title-box">
                    <span class="material-icons modal-icon" style="background: rgba(255,255,255,0.2); color: white;">assignment</span>
                    <div>
                        <h3 style="color: white; margin: 0;">${currentExamState.examTitle}</h3>
                        <p style="color: rgba(255,255,255,0.85); margin: 0.1rem 0 0 0;">Automated Skill Verification Exam</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="background: rgba(0,0,0,0.3); padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.85rem; font-weight: 700;">
                        ⏱️ <span id="examTimerDisplay">00:00</span>
                    </div>
                    <button class="modal-close-btn" style="color: white;" onclick="closeExamModal()">&times;</button>
                </div>
            </div>

            <!-- Progress Bar -->
            <div style="background: var(--bg-color); padding: 0.75rem 1.75rem; border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between;">
                <div style="font-size: 0.85rem; font-weight: 800; color: var(--text-muted);">
                    Question ${currentExamState.currentIndex + 1} of ${totalQ}
                </div>
                <div style="width: 250px; height: 8px; background: var(--border-color); border-radius: 4px; overflow: hidden;">
                    <div style="width: ${progressPct}%; height: 100%; background: linear-gradient(90deg, #10b981, #7c3aed); transition: width 0.3s;"></div>
                </div>
            </div>

            <!-- Question Area -->
            <div class="modal-body" style="flex: 1; overflow-y: auto; padding: 1.75rem;">
                <div style="background: var(--bg-color); border-left: 4px solid #7c3aed; padding: 1.25rem 1.5rem; border-radius: 0 12px 12px 0; margin-bottom: 1.5rem;">
                    <span style="font-size: 0.75rem; font-weight: 800; color: #7c3aed; text-transform: uppercase; letter-spacing: 0.5px;">Chapter ${q.chapter} Scenario</span>
                    <h4 style="font-size: 1.1rem; font-weight: 800; color: var(--text-main); margin: 0.4rem 0 0 0; line-height: 1.45;">${q.question}</h4>
                </div>

                <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                    ${optionsHtml}
                </div>
            </div>

            <!-- Navigation Footer -->
            <div style="padding: 1.25rem 1.75rem; border-top: 1px solid var(--border-color); background: var(--bg-card); display: flex; justify-content: space-between; align-items: center;">
                <button class="btn-secondary" onclick="prevExamQuestion()" ${currentExamState.currentIndex === 0 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>
                    <span class="material-icons">arrow_back</span> Previous Question
                </button>

                <div style="display: flex; gap: 0.75rem;">
                    ${currentExamState.currentIndex < totalQ - 1 
                        ? `<button class="btn-primary-send" onclick="nextExamQuestion()">Next Question <span class="material-icons">arrow_forward</span></button>`
                        : `<button class="btn-primary-send" style="background: linear-gradient(135deg, #10b981, #059669);" onclick="submitExam()">🏆 Submit Exam & Get Certificate</button>`
                    }
                </div>
            </div>
        </div>
    `;

    modal.style.display = 'flex';
}

function selectExamOption(idx) {
    currentExamState.userAnswers[currentExamState.currentIndex] = idx;
    renderExamModal();
}

function prevExamQuestion() {
    if (currentExamState.currentIndex > 0) {
        currentExamState.currentIndex--;
        renderExamModal();
    }
}

function nextExamQuestion() {
    if (currentExamState.currentIndex < currentExamState.questions.length - 1) {
        currentExamState.currentIndex++;
        renderExamModal();
    }
}

function closeExamModal() {
    if (confirm("Are you sure you want to exit the exam? Your progress will be reset.")) {
        if (currentExamState.timerInterval) clearInterval(currentExamState.timerInterval);
        const modal = document.getElementById('examRunnerModalOverlay');
        if (modal) modal.style.display = 'none';
    }
}

function submitExam() {
    if (currentExamState.timerInterval) clearInterval(currentExamState.timerInterval);

    const questions = currentExamState.questions;
    let correctCount = 0;
    const totalQ = questions.length;

    questions.forEach((q, idx) => {
        if (currentExamState.userAnswers[idx] === q.answer) {
            correctCount++;
        }
    });

    const percentage = Math.round((correctCount / totalQ) * 100);
    const passed = percentage >= currentExamState.passingScorePct;

    renderExamResults(correctCount, totalQ, percentage, passed);
}

function renderExamResults(correctCount, totalQ, percentage, passed) {
    const modal = document.getElementById('examRunnerModalOverlay');
    if (!modal) return;

    let reviewHtml = '';
    currentExamState.questions.forEach((q, idx) => {
        const userAns = currentExamState.userAnswers[idx];
        const isCorrect = userAns === q.answer;
        const icon = isCorrect ? 'check_circle' : 'cancel';
        const color = isCorrect ? '#10b981' : '#ef4444';

        reviewHtml += `
            <div style="background: var(--bg-color); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; margin-bottom: 1rem; border-left: 4px solid ${color};">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span style="font-size: 0.8rem; font-weight: 800; color: ${color}; display: flex; align-items: center; gap: 0.3rem;">
                        <span class="material-icons" style="font-size: 1rem;">${icon}</span> Question ${idx + 1} - ${isCorrect ? 'Correct' : 'Incorrect'}
                    </span>
                    <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600;">Chapter ${q.chapter}</span>
                </div>
                <h5 style="font-size: 0.95rem; font-weight: 700; color: var(--text-main); margin: 0 0 0.6rem 0;">${q.question}</h5>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0 0 0.4rem 0;">
                    <strong>Your Answer:</strong> ${userAns !== undefined ? q.options[userAns] : 'Not Answered'}
                </p>
                <p style="font-size: 0.85rem; color: #10b981; font-weight: 700; margin: 0 0 0.5rem 0;">
                    <strong>Correct Answer:</strong> ${q.options[q.answer]}
                </p>
                <div style="background: rgba(124, 58, 237, 0.06); padding: 0.6rem 0.85rem; border-radius: 6px; font-size: 0.82rem; color: var(--text-main);">
                    💡 <strong>Explanation:</strong> ${q.explanation}
                </div>
            </div>
        `;
    });

    const certBtnHtml = passed ? `
        <button class="btn-primary-send" style="background: linear-gradient(135deg, #10b981, #059669); padding: 0.75rem 1.5rem; font-size: 1rem;" onclick="generateOfficialCertificate('${percentage}')">
            🎓 Download / Print Official Certificate
        </button>
    ` : `
        <button class="btn-primary-send" onclick="launchExam('${currentExamState.examType}')">
            🔄 Retake Exam
        </button>
    `;

    modal.innerHTML = `
        <div class="contact-modal" style="max-width: 850px; height: 90vh; max-height: 800px; display: flex; flex-direction: column;">
            <div class="modal-header" style="background: ${passed ? 'linear-gradient(135deg, #10b981, #059669)' : 'linear-gradient(135deg, #ef4444, #dc2626)'}; color: white;">
                <div class="modal-title-box">
                    <span class="material-icons modal-icon" style="background: rgba(255,255,255,0.2); color: white;">
                        ${passed ? 'emoji_events' : 'error_outline'}
                    </span>
                    <div>
                        <h3 style="color: white; margin: 0;">${passed ? '🎉 Congratulations! You Passed!' : 'Exam Results - Keep Practicing'}</h3>
                        <p style="color: rgba(255,255,255,0.9); margin: 0.1rem 0 0 0;">${currentExamState.examTitle}</p>
                    </div>
                </div>
                <button class="modal-close-btn" style="color: white;" onclick="document.getElementById('examRunnerModalOverlay').style.display='none'">&times;</button>
            </div>

            <!-- Score Summary Card -->
            <div style="background: var(--bg-card); padding: 1.5rem 2rem; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-around; align-items: center; text-align: center;">
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: ${passed ? '#10b981' : '#ef4444'};">${percentage}%</div>
                    <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Final Score</div>
                </div>
                <div style="height: 40px; width: 1px; background: var(--border-color);"></div>
                <div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: var(--text-main);">${correctCount} / ${totalQ}</div>
                    <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Correct Answers</div>
                </div>
                <div style="height: 40px; width: 1px; background: var(--border-color);"></div>
                <div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: var(--text-main);">${currentExamState.passingScorePct}%</div>
                    <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Passing Threshold</div>
                </div>
            </div>

            <!-- Questions Review -->
            <div class="modal-body" style="flex: 1; overflow-y: auto; padding: 1.75rem;">
                <h4 style="font-size: 1.05rem; font-weight: 800; color: var(--text-main); margin: 0 0 1rem 0;">Detailed Performance Breakdown</h4>
                ${reviewHtml}
            </div>

            <!-- Footer Actions -->
            <div style="padding: 1.25rem 1.75rem; border-top: 1px solid var(--border-color); background: var(--bg-card); display: flex; justify-content: space-between; align-items: center;">
                <button class="btn-secondary" onclick="document.getElementById('examRunnerModalOverlay').style.display='none'">Close Window</button>
                ${certBtnHtml}
            </div>
        </div>
    `;
}

function generateOfficialCertificate(scorePct) {
    const userName = prompt("Please enter your full name for the Official Certificate:", "Abhineet Kumar Singh") || "IT Specialist";

    const certWindow = window.open("", "_blank");
    const today = new Date().toLocaleDateString("en-GB", { day: 'numeric', month: 'long', year: 'numeric' });
    const certId = "CERT-" + Math.floor(100000 + Math.random() * 900000);

    certWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Official Certificate of Completion - ${userName}</title>
            <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Playfair+Display:ital,wght@1,700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Plus Jakarta Sans', sans-serif;
                    background: #f1f5f9;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 2rem;
                    margin: 0;
                }
                .certificate-card {
                    background: #ffffff;
                    width: 1000px;
                    padding: 3.5rem;
                    border-radius: 20px;
                    border: 12px solid #005eb8;
                    box-shadow: 0 20px 60px rgba(0,0,0,0.15);
                    position: relative;
                    text-align: center;
                    box-sizing: border-radius;
                }
                .inner-border {
                    border: 2px solid #d97706;
                    padding: 2.5rem;
                    border-radius: 12px;
                }
                .cert-title {
                    font-family: 'Cinzel', serif;
                    font-size: 2.4rem;
                    font-weight: 800;
                    color: #005eb8;
                    letter-spacing: 2px;
                    margin-bottom: 0.5rem;
                }
                .cert-subtitle {
                    font-size: 1rem;
                    font-weight: 700;
                    color: #7c3aed;
                    text-transform: uppercase;
                    letter-spacing: 3px;
                    margin-bottom: 2rem;
                }
                .cert-recipient {
                    font-family: 'Playfair Display', serif;
                    font-size: 3rem;
                    font-weight: 700;
                    color: #0f172a;
                    margin: 1.5rem 0;
                    border-bottom: 2px solid #e2e8f0;
                    display: inline-block;
                    padding-bottom: 0.5rem;
                }
                .cert-body {
                    font-size: 1.1rem;
                    color: #475569;
                    max-width: 750px;
                    margin: 0 auto 2.5rem auto;
                    line-height: 1.6;
                }
                .cert-footer {
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-end;
                    margin-top: 3rem;
                    padding-top: 1.5rem;
                    border-top: 1px solid #e2e8f0;
                }
                .sig-box { text-align: center; }
                .sig-line { width: 220px; border-top: 2px solid #0f172a; margin-bottom: 0.4rem; }
                .sig-title { font-size: 0.9rem; font-weight: 800; color: #0f172a; }
                .sig-subtitle { font-size: 0.8rem; color: #64748b; }
                .cert-seal {
                    width: 90px; height: 90px;
                    background: linear-gradient(135deg, #d97706, #7c3aed);
                    color: white; border-radius: 50%;
                    display: flex; align-items: center; justify-content: center;
                    font-weight: 800; font-size: 0.85rem; text-align: center;
                    box-shadow: 0 4px 15px rgba(217, 119, 6, 0.3);
                }
                @media print {
                    body { background: white; padding: 0; }
                    .certificate-card { box-shadow: none; width: 100%; border-width: 8px; }
                }
            </style>
        </head>
        <body>
            <div class="certificate-card">
                <div class="inner-border">
                    <div class="cert-title">CERTIFICATE OF ACHIEVEMENT</div>
                    <div class="cert-subtitle">IT SERVICE DESK & AI OPERATIONS MASTERY</div>
                    
                    <p style="font-size: 1rem; color: #64748b; margin: 0;">This is to certify that</p>
                    <div class="cert-recipient">${userName}</div>
                    
                    <div class="cert-body">
                        has successfully passed the comprehensive <strong>IT Service Desk & AI Operations Certification Exam</strong> with a score of <strong>${scorePct}%</strong>, demonstrating mastery in Helpdesk Operations, Microsoft Intune, Incident Management, ITIL Frameworks, and AI Virtual Agent Automation.
                    </div>

                    <div class="cert-footer">
                        <div class="sig-box">
                            <div style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: #005eb8; font-weight: 700; margin-bottom: 0.2rem;">Abhineet Singh</div>
                            <div class="sig-line"></div>
                            <div class="sig-title">Abhineet Singh</div>
                            <div class="sig-subtitle">IT Operations Manager & Course Director</div>
                        </div>

                        <div class="cert-seal">
                            OFFICIAL<br>VERIFIED
                        </div>

                        <div style="text-align: right; font-size: 0.85rem; color: #64748b;">
                            <div><strong>Date Issued:</strong> ${today}</div>
                            <div><strong>Certificate ID:</strong> ${certId}</div>
                            <div><strong>Verification:</strong> Passed (${scorePct}%)</div>
                        </div>
                    </div>
                </div>
            </div>
            <script>
                window.onload = function() { window.print(); };
            </script>
        </body>
        </html>
    `);
}
