from core.data_reader import DataReader as dr
from core.analyzer import DataAnalyzer as da

data = dr.read_data_from_file()  # type: ignore
print(da.analyzer(data))
