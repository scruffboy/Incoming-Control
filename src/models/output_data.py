from datetime import datetime


class OutputData:
    """
    Class for processed data for output
    """

    def __init__(
        self,
        date: datetime,
        document_number: str,
        supplier: str,
        group_product: str,
        temp: str,
    ):
        self.date = date
        self.document_number = document_number
        self.supplier = supplier
        self.group_product = group_product
        self.temp = temp
        self.mark_1 = "V"
        self.mark_2 = "V"
        self.mark_3 = "V"
        self.mark_4 = "V"
