from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, DateTime, String, ForeignKey
from api.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    agreement_id: Mapped[str] = mapped_column(String(10), nullable=True, index=True)
    
    promo_price: Mapped[float] = mapped_column(Float)
    promo_ir: Mapped[float] = mapped_column(Float)
    
    promo_start: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    promo_end: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    
    
    