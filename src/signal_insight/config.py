from pathlib import Path

WORKSPACE_MARKER = "signal.workspace"

def find_project_root(marker: str = WORKSPACE_MARKER) -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(
        f"未找到项目根标记文件 {marker!r}，请确认它存在于项目根目录"
    )

PROJECT_ROOT = find_project_root()

DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "signal.db"  # 探索库
# 检查库，前一天没做完可以从这里恢复
CHECKPOINT_DB = DATA_DIR / "checkpoints.db"

IMAGE_DIR = PROJECT_ROOT / "image"

UTC_OFFSET_HOURS = 8
ANALYSIS_DAY = "2018-10-03"
SOURCE_NOTE = "数据来源：沈阳移动信令样本(脱敏，2018年国庆)"
AUTHOR = "TeamSpirit"