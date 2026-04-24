from datetime import date
from dataclasses import dataclass


@dataclass
class OutputData:
    """
    Processed data model
    """

    date: date
    document_number: str
    supplier: str
    group_product: str
    temp: str
    packaging_condition: str = "V"
    accompanying_documents: str = "V"
    medical_book: str = "V"
    marking: str = "V"