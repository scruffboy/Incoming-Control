import logging
from src.core.creator import DataCreator
from src.core.analyzer import DataAnalyzer
from src.core.reader import DataReader
from src.utils.config import Config as conf


def test_creator_output_data():
    """ """
    df = DataReader.read_data_from_file(file_path=conf.TEST_PATH_TO_SAMPLE_FILE)
    load_data_list = DataAnalyzer.analyzer(df)
    output_data_list = DataCreator.create_output_data(load_data_list)

    assert isinstance(output_data_list, list)
    assert output_data_list[0].supplier == "ПепсиКо Холдингс"
