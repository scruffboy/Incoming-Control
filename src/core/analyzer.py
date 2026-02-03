import pandas as pd
from models.load_data import LoadData


class DataAnalyzer:
    """
    Docstring для Analyzer
    """

    @staticmethod
    def iii(data):
        """
        Docstring для iii

        :param data: Описание
        :type data: pd.DataFrame | str
        """
        load_data_objects = []

        if isinstance(data, pd.DataFrame):
            load_data_objects = data.apply(
                lambda row: LoadData(
                    date=row.iloc[0],
                    supplier=row.iloc[1],
                    storage=row.iloc[2],
                    document_number=row.iloc[3],
                ),
                axis=1,
            ).tolist()

        return load_data_objects
