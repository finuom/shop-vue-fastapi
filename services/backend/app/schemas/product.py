from pydantic import BaseModel
from typing import Optional

# Base schema for input (POST/PUT)
class ProductIn(BaseModel):
    title: str
    subtitle: str
    source: Optional[str] = None
    price: float
    qtd: int
    category: str

# Output schema (includes ID)
class ProductOut(ProductIn):
    id: int

    class Config:
        orm_mode = True