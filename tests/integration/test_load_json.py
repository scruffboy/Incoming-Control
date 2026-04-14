from src.utils.helper import Utils as utls
from src.utils.config import Config as conf


def test_load_json():
    """
    Checking data loading from a JSON file
    """
    supplier_data = utls.load_json(conf.SUPPLIERS_JSON)

    assert isinstance(supplier_data, dict)
    assert supplier_data["suppliers"][0]["name"] == "Агама Истра"
