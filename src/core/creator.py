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
    def _determine_group_and_temp(
        suppliers: str, storage: str, mapping: dict
    ) -> Tuple[str, str]:
        """
        Determines product group and temperature by warehouse and supplier
        """
        logger.debug(
            f"Determining group/temp for supplier: '{suppliers}' (Storage: '{storage}')."
        )
        if conf.DRY_STORAGE.lower() in storage.lower():
            logger.debug(f"The group/temp defined: 'Сухие, +18°C'")
            return ("Сухие", "+18°C")

        options = mapping.get(suppliers, {}).get("options", [])

        # TODO: Implement logic for selecting a product group/temperature based on items from the invoice
        logger.debug(f"A stub is used!")
        if options:
            choice = options[0]

            logger.debug(
                f"Group/temp defined: {choice.get("group", "None")}, {choice.get("temperature", "0°C")}"
            )
            return choice.get("group", "None"), choice.get("temperature", "0°C")

        logger.error(f"Group and temp not defined!")
        return "None", "0°C"

    @staticmethod
    def create_output_data(
        load_data_objects: List[LoadData],
    ) -> List[OutputData] | None:
        """
        Gets a list of LoadData objects and creates a new list of OutputData objects based on them
        """
        logger.info(f"Generation of output data...")
        logger.debug(f"Loading supplier data from '{conf.SUPPLIERS_JSON.name}'.")
        data = utls.load_json(conf.SUPPLIERS_JSON)

        logger.debug(f"Mapping by suppliers is being created...")
        mapping = {el["name"]: el for el in data.get("suppliers", [])} if data else {}

        output_object_list = []

        for obj in load_data_objects:
            if mapping.get(obj.supplier, None) is None:
                continue

            group, temp = DataCreator._determine_group_and_temp(
                obj.supplier, obj.storage, mapping
            )

            output_object_list.append(
                OutputData(
                    date=obj.date,
                    document_number=obj.document_number,
                    supplier=obj.supplier,
                    group_product=group,
                    temp=temp,
                )
            )

        logger.info(
            f"The output data has been generated. Total quantity: {len(output_object_list)}."
        )
        return output_object_list
