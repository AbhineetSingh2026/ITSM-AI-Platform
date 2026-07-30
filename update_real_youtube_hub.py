import re
from pathlib import Path

index_path = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform/index.html")
html = index_path.read_text(encoding="utf-8")

# 1. Update Subscribe link and Channel Info
html = html.replace(
    'href="https://www.youtube.com/results?search_query=The+AI+Driven+IT+Manager"',
    'href="https://www.youtube.com/@AIDrivenITManager"'
)

# 2. Build exact real video cards HTML for YouTube Hub
real_yt_section = """<section id="tab-youtube" class="tab-view hidden space-y-8 max-w-5xl mx-auto">
        <div class="glass-panel p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-6 bg-gradient-to-br from-cyberSlate to-cyberBg border border-red-500/30">
          <div class="space-y-4 flex-1">
            <div class="flex items-center gap-2">
              <span class="badge-neon border-red-500/40 text-red-400 bg-red-500/10"><i class="fa-brands fa-youtube text-red-500 animate-pulse"></i> Official YouTube Channel</span>
              <span class="text-xs font-mono text-slate-400">@AIDrivenITManager</span>
            </div>
            <h2 class="text-3xl font-bold text-white">The AI-Driven IT Manager</h2>
            <p class="text-slate-300 text-xs leading-relaxed max-w-xl">
              Hosted by Abhineet Singh (20+ Years IT Operations Leader). Subscribe for practical advice on ITSM processes, ITIL 4 frameworks, Halo ESM tutorials, and AI-driven Service Desk automation.
            </p>
            <div class="pt-2 flex items-center gap-4">
              <a href="https://www.youtube.com/@AIDrivenITManager" target="_blank" class="cyber-btn bg-red-600 hover:bg-red-700 shadow-red-600/30 text-white font-bold flex items-center gap-2 px-6 py-3 rounded-xl transition-all">
                <i class="fa-brands fa-youtube text-lg"></i> Subscribe @AIDrivenITManager
              </a>
              <span class="text-xs text-slate-400 font-mono"><i class="fa-solid fa-users text-cyberCyan"></i> 28 Subscribers • 4 Videos</span>
            </div>
          </div>
          <div class="w-48 h-48 border-2 border-red-500/40 rounded-full overflow-hidden shadow-2xl shrink-0 bg-slate-900 relative group">
            <img src="assets/profile.jpg" alt="Abhineet Singh - The AI-Driven IT Manager" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-black/40 group-hover:bg-black/10 transition-all flex items-center justify-center">
              <span class="w-10 h-10 rounded-full bg-red-600 text-white flex items-center justify-center text-sm shadow-lg"><i class="fa-brands fa-youtube"></i></span>
            </div>
          </div>
        </div>

        <!-- Real Uploaded YouTube Videos Grid -->
        <div class="space-y-6">
          <div class="flex justify-between items-center border-b border-slate-800 pb-3">
            <h3 class="text-xl font-bold text-white flex items-center gap-2">
              <i class="fa-brands fa-youtube text-red-500"></i> Latest Channel Videos & Tutorials
            </h3>
            <a href="https://www.youtube.com/@AIDrivenITManager/videos" target="_blank" class="text-xs text-cyberCyan hover:underline font-mono">View All Videos on YouTube <i class="fa-solid fa-arrow-up-right-from-square"></i></a>
          </div>

          <div id="youtube-video-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Video 1 -->
            <a href="https://www.youtube.com/@AIDrivenITManager" target="_blank" class="glass-panel p-4 space-y-3 group hover:border-red-500/50 transition-all duration-300 block">
              <div class="relative w-full h-44 rounded-xl overflow-hidden bg-slate-900 border border-white/[0.08]">
                <img src="assets/yt_thumb_1.png" alt="How AI Is Automating L1 Service Desk" class="w-full h-full object-cover group-hover:scale-105 transition-all duration-500">
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/10 transition-all flex items-center justify-center">
                  <span class="w-12 h-12 rounded-full bg-red-600/90 text-white flex items-center justify-center text-lg shadow-lg group-hover:scale-110 transition-all"><i class="fa-solid fa-play ml-1"></i></span>
                </div>
                <span class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 text-white font-mono text-[10px] font-bold">0:41</span>
              </div>
              <div class="space-y-1">
                <span class="text-[9px] font-bold uppercase tracking-wider text-red-400 font-mono">L1 Automation</span>
                <h4 class="text-xs font-bold text-white group-hover:text-red-400 transition-colors line-clamp-2 leading-snug">How AI Is Automating L1 Service Desk (Zero Touch IT Support)</h4>
                <p class="text-slate-400 text-[11px] line-clamp-2 leading-relaxed">How generative AI, autonomous ticket routing, and self-healing scripts are replacing manual L1 triage.</p>
              </div>
              <div class="flex items-center justify-between text-[10px] text-slate-500 font-mono border-t border-white/[0.05] pt-2">
                <span><i class="fa-solid fa-eye text-red-500"></i> 40 views</span>
                <span>2 months ago</span>
              </div>
            </a>

            <!-- Video 2 -->
            <a href="https://www.youtube.com/@AIDrivenITManager" target="_blank" class="glass-panel p-4 space-y-3 group hover:border-red-500/50 transition-all duration-300 block">
              <div class="relative w-full h-44 rounded-xl overflow-hidden bg-slate-900 border border-white/[0.08]">
                <img src="assets/yt_thumb_2.png" alt="AI in ITSM: Ticket Triage" class="w-full h-full object-cover group-hover:scale-105 transition-all duration-500">
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/10 transition-all flex items-center justify-center">
                  <span class="w-12 h-12 rounded-full bg-red-600/90 text-white flex items-center justify-center text-lg shadow-lg group-hover:scale-110 transition-all"><i class="fa-solid fa-play ml-1"></i></span>
                </div>
                <span class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 text-white font-mono text-[10px] font-bold">3:58</span>
              </div>
              <div class="space-y-1">
                <span class="text-[9px] font-bold uppercase tracking-wider text-cyberCyan font-mono">Service Desk Triage</span>
                <h4 class="text-xs font-bold text-white group-hover:text-red-400 transition-colors line-clamp-2 leading-snug">AI in ITSM: How to Reduce Manual Ticket Triage in a Service Desk</h4>
                <p class="text-slate-400 text-[11px] line-clamp-2 leading-relaxed">Practical insights on transitioning to a streamlined, AI-driven CTI triage structure.</p>
              </div>
              <div class="flex items-center justify-between text-[10px] text-slate-500 font-mono border-t border-white/[0.05] pt-2">
                <span><i class="fa-solid fa-eye text-red-500"></i> 89 views</span>
                <span>2 months ago</span>
              </div>
            </a>

            <!-- Video 3 -->
            <a href="https://www.youtube.com/@AIDrivenITManager" target="_blank" class="glass-panel p-4 space-y-3 group hover:border-red-500/50 transition-all duration-300 block">
              <div class="relative w-full h-44 rounded-xl overflow-hidden bg-slate-900 border border-white/[0.08]">
                <img src="assets/yt_thumb_3.png" alt="The Death of SLAs: XLAs Strategy" class="w-full h-full object-cover group-hover:scale-105 transition-all duration-500">
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/10 transition-all flex items-center justify-center">
                  <span class="w-12 h-12 rounded-full bg-red-600/90 text-white flex items-center justify-center text-lg shadow-lg group-hover:scale-110 transition-all"><i class="fa-solid fa-play ml-1"></i></span>
                </div>
                <span class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 text-white font-mono text-[10px] font-bold">4:08</span>
              </div>
              <div class="space-y-1">
                <span class="text-[9px] font-bold uppercase tracking-wider text-cyberPurple font-mono">XLA vs SLA Strategy</span>
                <h4 class="text-xs font-bold text-white group-hover:text-red-400 transition-colors line-clamp-2 leading-snug">The Death of SLAs: Why Modern IT Managers are Shifting to XLAs</h4>
                <p class="text-slate-400 text-[11px] line-clamp-2 leading-relaxed">Why SLA compliance can hide poor user experience and how Experience Level Agreements solve it.</p>
              </div>
              <div class="flex items-center justify-between text-[10px] text-slate-500 font-mono border-t border-white/[0.05] pt-2">
                <span><i class="fa-solid fa-eye text-red-500"></i> 26 views</span>
                <span>2 months ago</span>
              </div>
            </a>
          </div>
        </div>
      </section>"""

# Replace existing tab-youtube section with real youtube section
html = re.sub(
    r'<section id="tab-youtube".*?</section>',
    real_yt_section,
    html,
    flags=re.DOTALL
)

index_path.write_text(html, encoding="utf-8")
print("[OK] Updated YouTube Hub with real channel @AIDrivenITManager & real videos!")
