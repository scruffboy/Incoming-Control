from datetime import date
from dataclasses import dataclass


@dataclass
class LoadData:
    """
    Raw data model
    """

    date: date
    supplier: str
    storage: str
    document_number: str
