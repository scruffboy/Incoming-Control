import logging
from typing import List, Tuple
from src.models.output_data import OutputData
from src.models.load_data import LoadData
from src.utils.helper import Utils as utls
from src.utils.config import Config as conf


logger = logging.getLogger(__name__)


class DataCreator:
    """
    Output object creator model
    """

    @staticmethod
    def _get_group_and_temp() -> Tuple[str, str] | None:
        """"""
        suppliers_data = utls.load_json(conf.SUPPLIERS_JSON)

    @staticmethod
    def create_output_data(
        load_data_objects: List[LoadData],
    ) -> List[OutputData] | None:
        """
        Gets a list of LoadData objects and creates a new list of OutputData objects based on them
        """
        output_object_list = [
            OutputData(
                date=data.date,
                document_number=data.document_number,
                supplier=data.supplier,
                group_product="None",
                temp="-2",
            )
            for data in load_data_objects
        ]

        return output_object_list
