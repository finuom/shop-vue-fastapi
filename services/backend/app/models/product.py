from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base  # Importing the shared Base instance

class Product(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    subtitle = Column(String, nullable=False)
    source = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    qtd = Column(Integer, nullable=False)
    category = Column(String, nullable=False)