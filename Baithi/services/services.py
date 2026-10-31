from fastapi import HTTPException, APIRouter, FastAPI
from sqlalchemy.orm import Session
from database.database import declarative_base, get_db
from models.models import Cars, CarsType
from main import raw_cars
api = FastAPI()

router = APIRouter(
    prefix= "/cars",
    tags= "Cars"
)
@router.post("/POST/cars")
def add_cars(cars):
    add_code = input("Nhập code xe mới: ")
    for cars in raw_cars:
        if add_code == cars["car_code"]:
            print("Code này đã tồn tại!")
            return
    new_type = input("Nhập type cho xe mới: ")
    new_price = float(input("Nhập giá cho xe mới: "))
    new_status = input("Nhập trạng thái xe: ")

    new_cars = {
        "car_code": cars[add_code],
        "type": cars[new_type],
        "price": cars[new_price],
        "status": cars[new_status]
    }
    raw_cars.append(new_cars)
    print("Thêm xe mới thành công!")
