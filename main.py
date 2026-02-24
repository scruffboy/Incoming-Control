from src.core.data_reader import DataReader as dr
from src.core.analyzer import DataAnalyzer as da
from src.core.creator import DataCreator as dc
from src.core.writer import DataWriter as dw

data = dr.read_data_from_file()
data_2 = da.analyzer(data)
data_3 = dc.create_output_data(data_2)
dw.writing_output_data_to_excel(data_3)
