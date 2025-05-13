from app.schemas.product import ProductIn, ProductOut
from app.services.product_service import get_products, add_product, update_product, delete_product
from fastapi import APIRouter

router = APIRouter()

# Get all products
@router.get("/", response_model=list[ProductOut])
def get_products_():
    return get_products()

# Add product
@router.post("/", response_model=ProductOut)
def add_product_(product: ProductIn):
    return add_product(product)

# Update product
@router.put("/{product_id}", response_model=ProductOut)
def update_product_(product_id: int, product: ProductIn):
    return update_product(product_id, product)

# Delete product
@router.delete("/{product_id}")
def delete_product_(product_id: int):
    return delete_product(product_id)

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