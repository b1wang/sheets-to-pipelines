from fastapi import FastAPI, APIRouter, Depends
from typing import List, Optional
from pydantic import BaseModel

from app.database import Base, engine
from app.routers import product
from app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"Hello:": "World"}

app.include_router(product.router, prefix="/products", tags=["Products"])


