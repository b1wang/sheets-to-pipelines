from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from .schemas import ProductRead, ProductCreate, ProductDelete
from . import service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductRead, tags=["products"], summary="Insert a new product")
def create(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Insert a new product and expire old records.
    
    - **sku**: Product's SKU (required)
    - **asin**: Product's Amazon Identifier Number (Optional)
    - **msrp**: Product's MSRP
    - **list_price**: Product's List Price
    - **cost**: Product's cost
    """
    return service.upsert_product(db, product)

@router.get("/", response_model=list[ProductRead], tags=["products"], summary="Read all products")
def read_all(db: Session = Depends(get_db)):
    """
    Get list of current active SKUs.
    """
    return service.get_current_products(db)

@router.get("/{sku}", response_model=ProductRead, tags=["products"], summary="Query a single product")
def read_product_by_sku(sku: str, db: Session = Depends(get_db)):
    """
    Retrieve the current version of a product by SKU.
    
    - **sku**: Product SKU to look up
    """
    product = service.get_current_product_by_sku(db, sku)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with SKU '{sku}' not found.")
    return product

@router.put("/", response_model=ProductRead, tags=["products"], summary="Upsert a product")
def update(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Insert a new product and expire old records. (Same functionality as POST)
    
    - **sku**: Product's SKU (required)
    - **asin**: Product's Amazon Identifier Number (Optional)
    - **msrp**: Product's MSRP
    - **list_price**: Product's List Price
    - **cost**: Product's cost
    """
    return service.upsert_product(db, product)

@router.delete("/", response_model=ProductRead, tags=["products"], summary="Delete a product based on product id")
def delete_product(product: ProductDelete, db: Session = Depends(get_db)):
    """
    Delete a product by product_id
    
    - **id**: Product ID (required)
    """
    return service.delete_product_by_sku(db, product)