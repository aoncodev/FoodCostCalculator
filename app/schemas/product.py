from pydantic import BaseModel, Field, field_validator
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: int = Field(..., gt=0, description="Price must be a positive number")
    quantity: int = Field(..., gt=0, description="Quantity for which the price is defined")
    unit: str
    stock_quantity: int = Field(..., ge=0, description="Stock quantity must be 0 or greater")
    category: Optional[str] = None
    reorder_level: Optional[int] = Field(..., ge=0, description="Reorder level must be 0 or greater")
    is_Stock: bool = True

    # Validator to ensure only 'g' or 'ml' are accepted as units
    @field_validator('unit')
    def validate_unit(cls, v):
        if v not in ('g', 'ml'):
            raise ValueError('Unit must be either "g" or "ml"')
        return v

    @property
    def total_price(self):
        return self.stock_quantity * self.price

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str]
    price: Optional[int] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, gt=0)
    unit: Optional[str]
    stock_quantity: Optional[int] = Field(None, ge=0)
    reorder_level: Optional[int] = Field(None, ge=0)
    is_Stock: Optional[bool]

class ProductInDB(ProductBase):
    id: int


    class Config:
        from_attributes = True
