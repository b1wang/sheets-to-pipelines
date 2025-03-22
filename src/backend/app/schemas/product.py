from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    sku: str
    asin: Optional[str] = None
    msrp: float
    cost: float

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    valid_from: datetime
    valid_to: datetime | None
    is_current: bool

    class Config:
        from_attributes = True