import shutil
from pathlib import Path

workspace_dir = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")
assets_vid_dir = workspace_dir / "assets" / "videos"
assets_vid_dir.mkdir(parents=True, exist_ok=True)

yt_dir = Path(r"C:\ANTIGRAVITY_ABHINEET\MY_EARNING\You tube Channel")

v1 = yt_dir / "How AI is Automating L1 Service Desk (Zero-Touch IT Support).mp4"
v2 = yt_dir / "Why the Traditional IT Service Desk is Dying (Top 3 AI Automations).mp4"
v3 = yt_dir / "The Death of SLAs Why Modern IT Managers are Shifting to XLAs (Experience Level Agreements).mp4"

if v1.exists():
    shutil.copy2(v1, assets_vid_dir / "video_1.mp4")
    print(f"[OK] Copied {v1.name} -> assets/videos/video_1.mp4 ({v1.stat().st_size} bytes)")

if v2.exists():
    shutil.copy2(v2, assets_vid_dir / "video_2.mp4")
    print(f"[OK] Copied {v2.name} -> assets/videos/video_2.mp4 ({v2.stat().st_size} bytes)")

if v3.exists():
    shutil.copy2(v3, assets_vid_dir / "video_3.mp4")
    print(f"[OK] Copied {v3.name} -> assets/videos/video_3.mp4 ({v3.stat().st_size} bytes)")

print("\nAssets video directory populated successfully!")
