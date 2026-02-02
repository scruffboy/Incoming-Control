from datetime import datetime


class LoadData:
    """
    Class for raw input data
    """

    def __init__(
        self, date: datetime, supplier: str, storage: str, document_number: str
    ):
        self.date = date
        self.supplier = supplier
        self.storage = storage
        self.document_number = document_number
