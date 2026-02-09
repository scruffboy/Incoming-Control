import logging
from src.utils.config import Config as conf


conf.PATH_TO_LOG_FILES.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(conf.PATH_TO_LOG_FILES, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
