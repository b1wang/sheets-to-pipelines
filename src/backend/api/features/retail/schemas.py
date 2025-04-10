from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RetailInventoryBase(BaseModel):
    product_id: int
    date: datetime
    in_building_qty: int
    tranship_qty: int
    usable_supply_incl_qty: int
    usable_supply_excl_qty: int
    on_order_qty: int

class RetailInventoryCreate(RetailInventoryBase):
    id: int
    valid_from: datetime
    valid_to: datetime | None
    is_current: bool

    class Config:
        from_attributes = True
        
class RetailInventoryUpdate(RetailInventoryBase):
    pass

class RetailInventoryOut(RetailInventoryBase):
    pass