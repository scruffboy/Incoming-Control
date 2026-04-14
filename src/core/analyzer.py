import pandas as pd
import logging
from typing import List
from src.models.load_data import LoadData
from src.utils.config import Config as conf
from src.utils.helper import Utils as utls


logger = logging.getLogger(__name__)


class DataAnalyzer:
    """
    Data analyzer model
    """

    @staticmethod
    def analyzer(data: pd.DataFrame | None) -> List[LoadData]:
        """
        Receives data as a dataframe object or a string object, and creates LoadData objects based on the data
        """
        if data is None:
            logger.error(f"Data is empty!")
            return []

        load_data_objects = []

        if isinstance(data, pd.DataFrame):
            logger.info(f"Data analyzed...")

            # Cleaning and consolidating spaces
            data = data.apply(
                lambda x: x.astype(str).str.replace(r"\s+", " ", regex=True).str.strip()
            )

            rows = data.values.tolist()
            load_data_objects = [
                LoadData(
                    date=utls.formatting_date(r[conf.DATE]),
                    supplier=r[conf.SUPPLIER],
                    storage=r[conf.STORAGE],
                    document_number=r[conf.DOCUMENT_NUM],
                )
                for r in rows
                if any(pd.notna(val) for val in r)
            ]

        logger.info(
            f"Data has been processed. Created {len(load_data_objects)} objects."
        )
        return load_data_objects
