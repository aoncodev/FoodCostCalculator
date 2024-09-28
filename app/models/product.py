from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from ..database import Base

from sqlalchemy import Boolean, Column, Integer, String, Float

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)  # Price per unit
    quantity = Column(Integer)  # Quantity for which the price is defined
    unit = Column(String)
    stock_quantity = Column(Integer)
    category = Column(String)
    reorder_level = Column(Integer)
    is_Stock = Column(Boolean)

    @property
    def total_price(self):
        return self.stock_quantity * self.price
