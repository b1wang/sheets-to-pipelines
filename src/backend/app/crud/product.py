from sqlalchemy.orm import Session
from sqlalchemy import update
from app.models.product import Product
from app.schemas.product import ProductCreate
from datetime import datetime

def create_product(db: Session, product: ProductCreate) -> Product:
    # Set existing versions to not current
    db.query(Product).filter(
        Product.sku == product.sku,
        Product.is_current == True
    ).update({
        Product.is_current: False,
        Product.valid_to: datetime.utcnow()
    })

    db_product = Product(
        sku=product.sku,
        asin=product.asin,
        msrp=product.msrp,
        cost=product.cost,
        is_current=True,
        valid_from=datetime.utcnow()
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_current_products(db: Session):
    return db.query(Product).filter(Product.is_current == True).all()