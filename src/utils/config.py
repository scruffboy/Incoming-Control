from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Config:

    # File paths
    DATA_DIR = PROJECT_ROOT / "src" / "data"

    PATH_TO_RAW_DATA_FILE = DATA_DIR / "test_2.xlsx"
    PATH_TO_THE_PROCESSED_DATA_FILE = DATA_DIR / "output_data_test.xlsx"

    # Test file paths
    TEST_DATA_DIR = PROJECT_ROOT / "tests" / "data"

    TEST_PATH_TO_SAMPLE_FILE = TEST_DATA_DIR / "test_sample_excel.xlsx"

    # Logger paths
    LOG_DIR = PROJECT_ROOT / "logs"
    PATH_TO_LOG_FILES = LOG_DIR / "app.log"

    # Name index
    DATE = 0
    SUPPLIER = 1
    STORAGE = 2
    DOCUMENT_NUM = 3
