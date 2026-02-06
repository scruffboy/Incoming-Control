from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Config:

    # File paths
    DATA_DIR = PROJECT_ROOT / "src" / "data"

    PATH_TO_RAW_DATA_FILE = DATA_DIR / "test_2.xlsx"
    PATH_TO_THE_PROCESSED_DATA_FILE = ""

    # Name index
    DATE = 0
    SUPPLIER = 1
    STORAGE = 2
    DOCUMENT_NUM = 3
