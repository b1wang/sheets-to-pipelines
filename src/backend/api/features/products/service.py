from sqlalchemy.orm import Session
from sqlalchemy import update
from datetime import datetime, timezone

from api.features.products.models import Product
from api.features.products.schemas import ProductCreate, ProductUpdate, ProductDelete

def _update_existing_entries(db: Session, product: ProductCreate):
    db.query(Product).filter(
        Product.sku == product.sku,
        Product.is_current
    ).update({
        Product.is_current: False,
        Product.valid_to: datetime.utcnow()
    })

def upsert_product(db: Session, product: ProductCreate) -> Product:
    """ Insert a product into the "Products" SCD Type 2 table and expire old records.

    Args:
        db (Session): Database session dependency 
        product (ProductCreate): Product 

    Returns:
        Product: Product model
    """
    # Set existing versions to not current  
    _update_existing_entries(db, product)
    db_product = Product(
        sku=product.sku,
        asin=product.asin,
        msrp=product.msrp,
        list_price=product.list_price,
        cost=product.cost,
        is_current=True,
        valid_from=datetime.now(timezone.utc)
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_current_products(db: Session):
    return db.query(Product).filter(Product.is_current).all()

def get_current_product_by_sku(db: Session, sku: str):
    return db.query(Product).filter(
        Product.sku == sku,
        Product.is_current
    ).first()

def update_product(db: Session, product: ProductUpdate) -> Product:
    return upsert_product(db, product)

def delete_product_by_sku(db: Session, product: ProductDelete):
    product_to_remove = db.query(Product).filter(Product.sku == product.sku).first()
    if product_to_remove:
        db.delete(product_to_remove)
        db.commit()