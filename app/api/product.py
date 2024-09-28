from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas, models

router = APIRouter()


@router.get("/products/", response_model=List[schemas.ProductInDB])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()  # Retrieve all products from the database
    if products is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return products

@router.get("/product/{product_id}", response_model=schemas.ProductInDB)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

