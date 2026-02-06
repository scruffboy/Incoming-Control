from datetime import date


class LoadData:
    """
    Class for raw input data
    """

    def __init__(self, date: date, supplier: str, storage: str, document_number: str):
        self.date = date
        self.supplier = supplier
        self.storage = storage
        self.document_number = document_number

    def __repr__(self):
        return f"{self.date}, {self.supplier}, {self.storage}, {self.document_number}"
