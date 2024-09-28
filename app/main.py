from fastapi import Depends, FastAPI 
from sqlalchemy.orm import Session
from .api import product
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(product.router, prefix="/api/v1", tags=["products"])


@app.get('/')
def root():
    return {"message": "Welcome to food cost calculator"}