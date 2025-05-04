from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float
from models import Product
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from database import init_db, SessionLocal

init_db()

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

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:5564"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get all products
@app.get("/products", response_model=list[ProductOut])
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

# Add product
@app.post("/products", response_model=ProductOut)
def add_product(product: ProductIn):
    db = SessionLocal()
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    return db_product

# Update product
@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductIn):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        db.close()
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.title = product.title
    db_product.subtitle = product.subtitle
    db_product.source = product.source
    db_product.price = product.price
    db_product.qtd = product.qtd
    db_product.category = product.category
    db.commit()
    db.refresh(db_product)
    db.close()
    return db_product

# Delete product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        db.close()
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    db.close()
    return {"detail": "Product deleted"}

# Optional: Populate items only if DB is empty
# def populate_db_once(db: Session):
#     if db.query(Item).first():
#         return
#     items = [
#         Item(id=1, title='Slim Fitness Fashion', subtitle='Chapéu Panamá Shangtung Casual Unissex Aba Larga', source='https://m.media-amazon.com/images/I/61biqqRtsfL._AC_UL320_.jpg', price=35.90, qtd=0, category='Unissex'),
#         Item(id=2, title='GEMVIE', subtitle='Chapéu Panamá de palha verão', source='https://m.media-amazon.com/images/I/81JkyFwqipL._AC_UL320_.jpg', price=45.00, qtd=0, category='Unissex'),
#         Item(id=3, title='Genérico', subtitle='Chapéu Pescador Camping Australiano', source='https://m.media-amazon.com/images/I/4152xzA-b6L._AC_UL320_.jpg', price=36.90, qtd=0, category='Unissex'),
#         Item(id=4, title='HHW', subtitle='Chapéu Country Rodeio Festa Cowboy Boiadeira Camurça Moda Unissex.', source='https://m.media-amazon.com/images/I/615plFGN8OL._AC_UL320_.jpg', price=38.00, qtd=0, category='Unissex'),
#         Item(id=5, title='Couros Allas', subtitle='Chapéu De Palha Carnaúba Natural Country Marcatto.', source='https://m.media-amazon.com/images/I/51KJ33Ts-4L._AC_UL320_.jpg', price=49.90, qtd=0, category='Unissex'),
#         Item(id=6, title='Adidas', subtitle='Chapéu Balde Utility Boonie Bucket Hat.', source='https://m.media-amazon.com/images/I/71mRuk8kDYS._AC_UL320_.jpg', price=393.11, qtd=0, category='Unissex'),
#         Item(id=7, title='Kouk Authentic', subtitle='Chapéu Fedora Panamá Aveludado Feltro Macio com Faixa Aba Larga.', source='https://m.media-amazon.com/images/I/611uRwBHxwL._AC_UL320_.jpg', price=64.99, qtd=0, category='Unissex'),
#         Item(id=8, title='Bogu Store', subtitle='Chapéu De Palha Chinês de Fibra Natural De Bambu Pescador.', source='https://m.media-amazon.com/images/I/71fGO8i7KqL._AC_UL320_.jpg', price=45.00, qtd=0, category='Unissex'),
#         Item(id=9, title='UTOWO', subtitle='Chapéu de Sol Feminino com Proteção UV e Abertura de Rabo de Cavalo', source='https://m.media-amazon.com/images/I/71KAmPL+zsL._AC_SX569_.jpg', price=67.18, qtd=0, category='Feminino'),
#         Item(id=10, title='Jorzer', subtitle='Chapéu de Cowgirl Branco Nupcial Ocidental Aba Larga', source='https://m.media-amazon.com/images/I/71sWzfUlR+L._AC_UL320_.jpg', price=113.86, qtd=0, category='Feminino'),
#         Item(id=11, title='Genérico', subtitle='Chapéu de Sol Infantil FPS 50+', source='https://m.media-amazon.com/images/I/61b2diEW7BL._AC_UL320_.jpg', price=89.90, qtd=0, category='Infantil'),
#         Item(id=12, title='Genérico', subtitle='Chapéu Infantil de Proteção Solar Azul Turquesa', source='https://m.media-amazon.com/images/I/717yoPwbcSL._AC_UL320_.jpg', price=89.90, qtd=0, category='Infantil'),
#
#     ]
#     db.add_all(items)
#     db.commit()

if __name__ == '__main__':
    from uvicorn import run
    run("main:app", host="127.0.0.1", port=8500, reload=True)