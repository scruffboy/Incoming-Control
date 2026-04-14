from src.core.reader import DataReader
from src.core.analyzer import DataAnalyzer
from src.utils.config import Config as conf


def test_analyzer_excel_valid():
    """
    Checking analysis of 'xlsx' files
    """
    df = DataReader.read_data_from_file(conf.TEST_PATH_TO_SAMPLE_FILE)
    load_data_list = DataAnalyzer.analyzer(df)

    assert load_data_list is not None
    assert len(load_data_list) == 50
    assert load_data_list[0].supplier == "ПепсиКо Холдингс"
