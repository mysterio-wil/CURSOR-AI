# Required imports for the application
from math import pi
from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.settings import settings
from app.schemas import Dish

# Global constants for business logic
LOWER_LIMIT = 10
UPPER_LIMIT = 20

# FastAPI application configuration
# Uses settings defined in settings.py
app = FastAPI(
    title=settings.APP_NAME,
    description="A simple FastAPI project",
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database for demonstration
# Contains a predefined list of menu items
dishes_db: List[Dish] = [
    Dish(id=1, name="Pizza Margherita", price=12.99),
    Dish(id=2, name="Pasta Carbonara", price=14.50),
    Dish(id=3, name="Caesar Salad", price=9.99),
    Dish(id=4, name="Tomato Soup", price=7.50),
    Dish(id=5, name="Mushroom Risotto", price=16.99)
]

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message and the application version.
    
    Returns:
        dict: A dictionary containing a welcome message and the application version
    """
    return {"message": "Welcome to FastAPI!", "version": settings.APP_VERSION}

@app.get("/health")
async def health_check():
    """
    Health check endpoint that returns the current status of the application.
    
    Returns:
        dict: A dictionary containing the application status, name, and debug mode
    """
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "debug_mode": settings.DEBUG,
    }

def calculate_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle given its radius.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        float: The area of the circle
    """
    return pi * radius * radius

def analyze_number(number: int) -> str:
    """
    Analyzes a number and returns its description.
    
    Args:
        number: The number to analyze
        
    Returns:
        str: A string describing the number's characteristics
    """
    if number <= 0:
        return "zero or negative"

    if number % 2 != 0:
        return "odd"

    if LOWER_LIMIT < number < UPPER_LIMIT:
        return "even between 10 and 20"
    elif number >= UPPER_LIMIT:
        return "even greater than 20"
    else:
        return "even less than 10"

def process_data(data: str) -> dict:
    """
    Processes data securely using JSON parsing.
    
    Args:
        data: String containing the data to process
        
    Returns:
        dict: Processed data or error message if parsing fails
    """
    try:
        import json
        return json.loads(data)
    except json.JSONDecodeError:
        return {"error": "Invalid data format"}

# =============================================
# CRUD Endpoints for Menu Items Management
# =============================================

@app.post("/dishes/", response_model=Dish, status_code=status.HTTP_201_CREATED)
async def create_dish(dish: Dish):
    """
    Creates a new menu item.
    
    Args:
        dish: The dish object to be created
        
    Returns:
        Dish: The created dish object
    """
    dishes_db.append(dish)
    return dish

@app.get("/dishes", response_model=List[Dish])
async def read_dishes():
    """
    Returns the complete list of menu items.
    
    Returns:
        List[Dish]: A list of all menu items
    """
    return dishes_db

@app.get("/dishes/{dish_id}", response_model=Dish)
async def read_dish(dish_id: int):
    """
    Returns a specific menu item based on its ID.
    
    Args:
        dish_id: The ID of the dish to retrieve
        
    Returns:
        Dish: The requested dish object
        
    Raises:
        HTTPException: If the dish with the given ID is not found
    """
    for dish in dishes_db:
        if dish.id == dish_id:
            return dish
    raise HTTPException(status_code=404, detail="Dish not found")

@app.put("/dishes/{dish_id}", response_model=Dish)
async def update_dish(dish_id: int, updated_dish: Dish):
    """
    Updates the information of an existing menu item.
    
    Args:
        dish_id: The ID of the dish to update
        updated_dish: The new dish information
        
    Returns:
        Dish: The updated dish object
        
    Raises:
        HTTPException: If the dish with the given ID is not found
    """
    for i, dish in enumerate(dishes_db):
        if dish.id == dish_id:
            dishes_db[i] = updated_dish
            return updated_dish
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Dish with ID {dish_id} not found"
    )

@app.delete("/dishes/{dish_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dish(dish_id: int):
    """
    Deletes a menu item.
    
    Args:
        dish_id: The ID of the dish to delete
        
    Raises:
        HTTPException: If the dish with the given ID is not found
    """
    for i, dish in enumerate(dishes_db):
        if dish.id == dish_id:
            dishes_db.pop(i)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Dish with ID {dish_id} not found"
    )
