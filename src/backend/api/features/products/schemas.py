from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductBatch(BaseModel):
    num_updated: int
    


class ProductBase(BaseModel):
    sku: str
    asin: Optional[str] = None
    msrp: float
    list_price: float
    cost: float

# For responses to the client (GET) 
class ProductRead(ProductBase):
    id: int
    valid_from: datetime
    valid_to: datetime | None
    is_current: bool

    class Config:
        from_attributes = True
        
# For incoming client requests (POST)
class ProductCreate(ProductBase):
    pass

# For incoming client requests (PUT)
class ProductUpdate(ProductBase):
    pass

class ProductDelete(BaseModel):
    sku: str