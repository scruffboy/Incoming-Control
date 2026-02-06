from datetime import date


class OutputData:
    """
    Class for processed data for output
    """

    def __init__(
        self,
        date: date,
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

    def __repr__(self) -> str:
        return f"{self.date}, {self.document_number}, {self.supplier}, {self.group_product}, {self.temp}, {self.mark_1}, {self.mark_2}, {self.mark_3}, {self.mark_4}"
