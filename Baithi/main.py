from fastapi import HTTPException, APIRouter
from sqlalchemy.orm import Session
from database.database import declarative_base, get_db


def get_home():
    print("API dang chay")
    return

raw_cars = [
    {"car_code": "C301", "type": "suv","rental_price": 12000000, "status": "available"},
    {"car_code": "c107", "type": "sedan","rental_price": 700000, "status": "available"},
    {"car_code": "C202", "type": "pickup","rental_price": 950000, "status": "rented"},
    {"car_code": "C102", "type": "sedan","rental_price": 6500000, "status": "mantenance"},
    {"car_code": "C302", "type": "suv","rental_price": 15000000, "status": "available"}
]