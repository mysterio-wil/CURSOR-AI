from pydantic import BaseModel
from typing import Optional

class Dish(BaseModel):
    """
    Represents a dish in the menu system.
    
    Attributes:
        id: Unique identifier for the dish
        name: Name of the dish
        price: Price of the dish
    """
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True  # Allows conversion from ORM objects
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Pizza Margherita",
                "price": 12.99
            }
        } 