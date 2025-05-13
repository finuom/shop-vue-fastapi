from app.core.database import SessionLocal
from app.schemas.product import ProductIn, ProductOut
from app.models.product import Product

def repo_get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

def repo_add_product(product: ProductIn):
    db = SessionLocal()
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    return db_product

def repo_update_product(product_id: int, product: ProductIn):
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

def repo_delete_product(product_id: int):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        db.close()
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    db.close()
    return {"detail": "Product deleted"}

