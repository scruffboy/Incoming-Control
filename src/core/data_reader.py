import pandas as pd
from src.utils.config import Config as conf


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
        data = None

        if file_path.exists():
            print(f"The file '{file_path.name}' exists.")
        else:
            print(f"The file '{file_path.name}' not found!")
            return None

        print(f"Trying to read file...")

        try:
            if file_path.suffix == ".xlsx":
                data = pd.read_excel(file_path, header=None)
                print(f"The file is recognized as 'xlsx'.\nSuccessfully read.")
                return data
            elif file_path.suffix == ".txt":
                data = file_path.read_text(encoding="utf-8")
                print(f"The file is recognized as 'txt'.\nSuccessfully read.")
                return data
            else:
                print(f"This file is not supported.")
                return None
        except Exception as e:
            print(f"Critical error while reading '{file_path.name}': {e}")
            return None
