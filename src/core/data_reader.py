import pandas as pd
from utils.config import Config as conf
from models.output_data import OutputData
from pathlib import Path


class DataReader:
    """
    Docstring для DataReader
    """

    @staticmethod
    def read_data_from_file():
        """
        Docstring для read_data_from_file
        """
        RAW_DATA_PATH = Path(conf.PATH_TO_RAW_DATA_FILE)

        content = pd.read_excel(RAW_DATA_PATH)

        print(content)
