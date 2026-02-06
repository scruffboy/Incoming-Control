import pandas as pd
from utils.config import Config as conf


class DataReader:
    """
    File Reader Model
    """

    @staticmethod
    def read_data_from_file() -> pd.DataFrame | str | None:
        """
        Reads raw data from a data file
        """
        path = conf.PATH_TO_RAW_DATA_FILE
        data = None

        if path.exists():
            print(f"The file '{path.name}' exists..")
        else:
            print(f"The file '{path.name}' not found!")
            return None

        try:
            if path.suffix == ".xlsx":
                data = pd.read_excel(path, header=None)
            elif path.suffix == ".txt":
                data = path.read_text(encoding="utf-8")
            else:
                return f"This file is not supported."
        except Exception as e:
            return f"Error: {e}"

        return data
