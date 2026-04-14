from src.db.connection import Base
from sqlalchemy import Column, Integer, String, Date, UniqueConstraint


class Entry(Base):
    """
    Database model for processed incoming documents
    """

    __tablename__ = "entry"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    document_number = Column(String)
    supplier = Column(String)
    group_product = Column(String)
    temp = Column(String)
    packaging_condition = Column(String)
    accompanying_documents = Column(String)
    medical_book = Column(String)
    marking = Column(String)

    __table_args__ = (
        UniqueConstraint("date", "document_number", "supplier", name="_unique_values_"),
    )

    def __repr__(self):
        return (
            f"<Entry(id={self.id}, supplier={self.supplier}), "
            f"Date={self.date}, doc={self.document_number}>"
        )
