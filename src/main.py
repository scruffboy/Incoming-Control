from core.data_reader import DataReader as dr
from core.analyzer import DataAnalyzer as da
from core.creator import DataCreator as dc


data = dr.read_data_from_file()
date_2 = da.analyzer(data)
print(dc.create_output_data(date_2))
