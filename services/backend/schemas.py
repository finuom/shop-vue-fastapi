from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    subtitle: str
    source: str
    price: float
    qtd: int
    category: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True