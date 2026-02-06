import pandas as pd
from models.load_data import LoadData
from typing import List
from utils.config import Config as conf
from utils.helper import Utils as utl


class DataAnalyzer:
    """
    Data analyzer model
    """

    @staticmethod
    def analyzer(data: pd.DataFrame | str | None) -> List[LoadData]:
        """
        Receives data as a dataframe object or a string object, and creates LoadData objects based on the data
        """
        if data is None:
            print(f"Warning: data is empty!")
            return []

        load_data_objects = []

        if isinstance(data, pd.DataFrame):
            rows = data.values.tolist()

            load_data_objects = [
                LoadData(
                    date=utl.formatting_date(r[conf.DATE]),
                    supplier=r[conf.SUPPLIER],
                    storage=r[conf.STORAGE],
                    document_number=r[conf.DOCUMENT_NUM],
                )
                for r in rows
                if any(pd.notna(val) for val in r)
            ]
        elif isinstance(data, str):
            pass

        return load_data_objects
