from typing import List, Tuple
from src.models.output_data import OutputData
from src.models.load_data import LoadData


class DataCreator:
    """
    Output object creator model
    """

    @staticmethod
    def _get_group_and_temp(supplier: str, temp: str) -> Tuple[str, str] | None:
        pass

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
