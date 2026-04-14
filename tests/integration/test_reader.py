import pandas as pd
from src.core.reader import DataReader
from src.utils.config import Config as conf


def test_reader_excel_valid():
    """
    Checking the reading of 'xlsx' files
    """
    df = DataReader.read_data_from_file(file_path=conf.TEST_PATH_TO_SAMPLE_FILE)

    assert isinstance(df, pd.DataFrame)
    assert df is not None
    assert len(df) == 50
    assert str(df.iloc[25, 1]) == "Хорека Сервис"
