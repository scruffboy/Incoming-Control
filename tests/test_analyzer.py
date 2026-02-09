from src.core.data_reader import DataReader as dr
from src.core.analyzer import DataAnalyzer as da
from src.utils.config import Config as conf


def test_analyzer_excel_valid():
    """
    Checking analysis of 'xlsx' files
    """
    df = dr.read_data_from_file(conf.TEST_PATH_TO_SAMPLE_FILE)
    load_data_list = da.analyzer(df)

    assert load_data_list is not None
    assert len(load_data_list) == 50
    assert load_data_list[0].supplier.replace("\xa0", " ") == "ПепсиКо Холдингс"
