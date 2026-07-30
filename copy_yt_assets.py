import shutil
from pathlib import Path

WORKSPACE_DIR = Path("c:/ANTIGRAVITY_ABHINEET/MY WORKSPACE/itsm-ai-platform")
ASSETS_DIR = WORKSPACE_DIR / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

YT_SRC_DIR = Path("C:/ANTIGRAVITY_ABHINEET/MY_EARNING/You tube Channel")

# Copy 01_L1_IS_DEAD.png
if (YT_SRC_DIR / "01_L1_IS_DEAD.png").exists():
    shutil.copy2(YT_SRC_DIR / "01_L1_IS_DEAD.png", ASSETS_DIR / "yt_thumb_1.png")
    print("[OK] Copied yt_thumb_1.png")

# Copy profile / video 2 thumbnail
if (YT_SRC_DIR / "03_AI_Flowchart.png").exists():
    shutil.copy2(YT_SRC_DIR / "03_AI_Flowchart.png", ASSETS_DIR / "yt_thumb_2.png")
    print("[OK] Copied yt_thumb_2.png")

# Copy youtube_thumbnail.png (SLAs ARE DEAD)
if (YT_SRC_DIR / "youtube_thumbnail.png").exists():
    shutil.copy2(YT_SRC_DIR / "youtube_thumbnail.png", ASSETS_DIR / "yt_thumb_3.png")
    print("[OK] Copied yt_thumb_3.png")
