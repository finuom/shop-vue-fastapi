from app.core.database import init_db, SessionLocal
from app.schemas.product import ProductIn, ProductOut
from app.repositories.product_repository import repo_get_products, repo_add_product, repo_update_product, repo_delete_product

init_db()

def get_products():
    return repo_get_products()

def add_product(product: ProductIn):
    return repo_add_product(product)

def update_product(product_id: int, product: ProductIn):
    return repo_update_product(product_id, product)

def delete_product(product_id: int):
    return repo_delete_product(product_id)

