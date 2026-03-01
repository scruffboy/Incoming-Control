import pandas as pd
import logging
from src.utils.config import Config as conf


logger = logging.getLogger(__name__)


class DataReader:
    """
    File Reader Model
    """

    @staticmethod
    def read_data_from_file(
        file_path=conf.PATH_TO_RAW_DATA_FILE,
    ) -> pd.DataFrame | str | None:
        """
        Reads raw data from a data file
        """
        if not file_path.exists():
            logger.error(f"File not found '{file_path.name}'!")
            return None

        logger.info(f"Reading file: '{file_path.name}'.")

        try:
            if file_path.suffix == ".xlsx":
                data = pd.read_excel(file_path, header=None)
                logger.info(f"File read: 'xlsx'.")
                return data
            elif file_path.suffix == ".txt":
                data = file_path.read_text(encoding="utf-8")
                logger.info(f"File read: 'txt'.")
                return data
            else:
                logger.error(f"Unsupported format: '{file_path.suffix}'!")
                return None
        except Exception:
            logger.exception(f"Critical error reading: {file_path.name}!")
            return None
