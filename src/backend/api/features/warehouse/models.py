from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime, Float, String, ForeignKey
from api.database import Base
from api.features.products.models import Product

class WarehouseShipment(Base):
    __tablename__ = "warehouse_shipments_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    quantity: Mapped[int] = mapped_column(Integer)
    unit_price: Mapped[float] = mapped_column(Float)
    item_cost: Mapped[float] = mapped_column(Float)
    customer_po: Mapped[str] = mapped_column(String)
    ship_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    invoice_num: Mapped[int] = mapped_column(Integer)
    
    product: Mapped[Product] = relationship(back_populates="warehouse_shipments")
    
class WarehouseInventory(Base):
    __tablename__ = "warehouse_inventory_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    quantity: Mapped[int] = mapped_column(Integer)

    product: Mapped[Product] = relationship(back_populates="warehouse_inventory")