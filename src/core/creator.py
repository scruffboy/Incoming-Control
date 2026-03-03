import logging
from typing import List
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
    def create_output_data(
        load_data_objects: List[LoadData],
    ) -> List[OutputData] | None:
        """
        Gets a list of LoadData objects and creates a new list of OutputData objects based on them
        """
        data = utls.load_json(conf.SUPPLIERS_JSON)
        mapping = {el["name"]: el for el in data.get("suppliers", [])} if data else {}

        output_object_list = [
            OutputData(
                date=obj.date,
                document_number=obj.document_number,
                supplier=obj.supplier,
                group_product=mapping.get(obj.supplier, {}).get("group", "None"),
                temp=mapping.get(obj.supplier, {}).get("temp", "0"),
            )
            for obj in load_data_objects
        ]

        return output_object_list
