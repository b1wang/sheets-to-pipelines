from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, DateTime, ForeignKey
from api.database import Base
from api.features.products.models import Product

class RetailInventory(Base):
    __tablename__ = "retail_inventory_table"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    in_building_qty: Mapped[int] = mapped_column(Integer)
    tranship_qty: Mapped[int] = mapped_column(Integer)
    usable_supply_incl_qty: Mapped[int] = mapped_column(Integer)
    usable_supply_excl_qty: Mapped[int] = mapped_column(Integer)
    on_order_qty: Mapped[int] = mapped_column(Integer)
    date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    product: Mapped[Product] = relationship(back_populates="retail_inventory")
    
class RetailSale(Base):
    __tablename__ = "retail_sales_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    quantity: Mapped[int] = mapped_column(Integer)
    from_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    to_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    product: Mapped[Product] = relationship(back_populates="retail_sales")