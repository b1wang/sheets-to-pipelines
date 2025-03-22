from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime, Boolean, func
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(String(100), index=True)
    asin: Mapped[str | None] = mapped_column(String(10), nullable=True, index=True)
    msrp: Mapped[float] = mapped_column(Float)
    cost: Mapped[float] = mapped_column(Float)
    valid_from: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now())
    valid_to: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_current: Mapped[bool] = mapped_column(Boolean, default=True)