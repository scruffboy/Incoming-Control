from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Config:
    """
    Docstring для Config
    """

    DATA_DIR = PROJECT_ROOT / "src" / "data"

    PATH_TO_RAW_DATA_FILE = DATA_DIR / "test_2.xlsx"
    PATH_TO_THE_PROCESSED_DATA_FILE = ""
