from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Config:

    # Base directory
    DATA_DIR = PROJECT_ROOT / "data"
    LOG_DIR = PROJECT_ROOT / "logs"

    # Subfolders
    RAW_DIR = DATA_DIR / "raw"
    PROCESSED_DIR = DATA_DIR / "processed"
    REF_DIR = DATA_DIR / "references"

    # Files
    PATH_TO_RAW_DATA_FILE = RAW_DIR / "test_2.xlsx"
    PATH_TO_THE_PROCESSED_DATA_FILE = PROCESSED_DIR / "output_data_test.xlsx"
    SUPPLIERS_JSON = REF_DIR / "suppliers.json"

    # Logs
    PATH_TO_LOGS_FILES = LOG_DIR / "app.log"

    # Tests
    TEST_DATA_DIR = PROJECT_ROOT / "tests" / "data"
    TEST_PATH_TO_SAMPLE_FILE = TEST_DATA_DIR / "test_sample_excel.xlsx"

    # Index
    DATE = 0
    SUPPLIER = 1
    STORAGE = 2
    DOCUMENT_NUM = 3
