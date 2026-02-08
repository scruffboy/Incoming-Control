import pandas as pd
from typing import List
from models.output_data import OutputData
from utils.config import Config as conf


class DataWriter:
    """
    Output writer model
    """

    @staticmethod
    def writing_output_data_to_excel(output_object_list: List[OutputData]):
        """
        Writes output to an excel file
        """
        data = [vars(obj) for obj in output_object_list]
        df = pd.DataFrame(data)

        conf.PATH_TO_THE_PROCESSED_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        df.to_excel(
            conf.PATH_TO_THE_PROCESSED_DATA_FILE,
            index=False,
            sheet_name="Входной контроль",
            engine="openpyxl",
        )
