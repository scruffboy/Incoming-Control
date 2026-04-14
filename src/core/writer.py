import pandas as pd
import logging
from typing import List
from src.models.output_data import OutputData
from src.utils.config import Config as conf
from src.utils.helper import Utils as utls
from openpyxl.styles import Alignment


logger = logging.getLogger(__name__)


class DataWriter:
    """
    Output writer model
    """

    @staticmethod
    def writing_output_data_to_excel(output_object_list: List[OutputData] | None):
        """
        Writes output to an excel file
        """
        if not output_object_list:
            logger.error(f"No data to record!\nCancelling the operation.")
            return

        data = utls.formatting_obj_into_dict(output_object_list)
        df = pd.DataFrame(data)
        df.columns = conf.EXCEL_COLUMNS

        conf.PATH_TO_THE_PROCESSED_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Recording process...")
        with pd.ExcelWriter(
            conf.PATH_TO_THE_PROCESSED_DATA_FILE, engine="openpyxl"
        ) as writer:
            df.to_excel(writer, index=False, sheet_name="Входной контроль")

            sheet = writer.sheets["Входной контроль"]

            for cell in sheet[1]:
                cell.alignment = Alignment(text_rotation=90)

            sheet.row_dimensions[1].height = 200
