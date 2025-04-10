from fastapi import FastAPI, APIRouter, Depends
from typing import List, Optional

from api.database import Base, engine

from api.features.products.routers import router as products_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"Hello:": "World"}

app.include_router(products_router, prefix="/products", tags=["products"])


