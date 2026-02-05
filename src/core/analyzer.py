import pandas as pd
from models.load_data import LoadData
from typing import List
from utils.config import Config as conf


class DataAnalyzer:
    """
    Docstring для Analyzer
    """

    @staticmethod
    def analyzer(data: pd.DataFrame | str | None) -> List[LoadData]:
        """
        Docstring для iii

        :param data: Описание
        :type data: pd.DataFrame | str
        """
        if data is None:
            print(f"Warning: data is empty!")
            return []

        load_data_objects = []

        if isinstance(data, pd.DataFrame):
            rows = data.values.tolist()

            load_data_objects = [
                LoadData(
                    date=r[conf.DATE],
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
