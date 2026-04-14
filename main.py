import logging
from src.core.reader import DataReader
from src.core.analyzer import DataAnalyzer
from src.core.creator import DataCreator
from src.core.writer import DataWriter
from src.db.repository import DatabaseInteraction
from src.db.connection import DatabaseConnection
from src.tools.logger import setup_logging


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Program initialization...")
    DatabaseConnection.init_db()

    raw_data = DataReader.read_data_from_file()
    load_object_list = DataAnalyzer.analyzer(raw_data)
    output_object_list = DataCreator.create_output_data(load_object_list)

    DataWriter.writing_output_data_to_excel(output_object_list)
    DatabaseInteraction.add_all(output_object_list)
    logger.info("The program has been completed.")


if __name__ == "__main__":
    main()
