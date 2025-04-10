from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime, Boolean, func
from api.database import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    
    sku: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    asin: Mapped[str | None] = mapped_column(String(10), nullable=True, index=True)
    
    msrp: Mapped[float] = mapped_column(Float, nullable=False)
    list_price: Mapped[float] = mapped_column(Float, nullable=False)
    cost: Mapped[float] = mapped_column(Float, nullable=False)
    
    valid_from: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now())
    valid_to: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_current: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    
    retail_inventory: Mapped[list["RetailInventory"]] = relationship(back_populates="product")
    retail_sales: Mapped[list["RetailSale"]] = relationship(back_populates="product")
    warehouse_shipments: Mapped[list["WarehouseShipment"]] = relationship(back_populates="product")
    warehouse_inventory: Mapped[list["WarehouseInventory"]] = relationship(back_populates="product")
    
    