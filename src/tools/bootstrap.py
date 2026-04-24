import logging
from src.utils.config import Config as conf


logger = logging.getLogger(__name__)


def init_project_structure():
    """
    Initializing the required directory
    """
    for directory in conf.REQUIRED_DIR:
        try:
            if not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)
                logger.debug(f"Created: '{directory}'.")
            else:
                logger.debug(f"'{directory}' exists.")
        except PermissionError:
            logger.error(f"Permission denied: Could not create: '{directory}'!")
        except Exception as e:
            logger.error(f"Unknow error: '{e}'!")
