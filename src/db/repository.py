import logging
from typing import List
from sqlalchemy.dialects.sqlite import insert as sq_insert
from src.db.connection import DatabaseConnection
from src.db.db_models import Entry
from src.utils.helper import Utils as utls


logger = logging.getLogger(__name__)


class DatabaseInteraction:
    """
    Database interactions model
    """

    @classmethod
    def add_all(cls, data_list: List | None):
        """
        Adds array data to the database
        """
        if not data_list:
            logger.warning(f"Warning! There is no data to write to the database.")
            return

        dict_list = utls.formatting_obj_into_dict(data_list)

        # Batch constant
        BATCH_SIZE = 500

        for i in range(0, len(dict_list), BATCH_SIZE):
            batch = dict_list[i : i + BATCH_SIZE]
            with DatabaseConnection.session_scope() as session:
                stmt = sq_insert(Entry).values(batch)
                stmt = stmt.on_conflict_do_nothing(
                    index_elements=["date", "document_number", "supplier"]
                )
                session.execute(stmt)

        logger.info(f"Successfully! The data has been saved to the database.")
