import pytest
from src.tools.logger import setup_logging


@pytest.fixture(scope="session", autouse=True)
def manage_logger():
    setup_logging()
