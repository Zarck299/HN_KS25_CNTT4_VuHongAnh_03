from abc import ABC
from main import raw_cars
def search_cars(cars):
    search_code = input("Nhập code xe cần tìm: ")
    found = False
    for cars in raw_cars:
        if search_code is None:
            print("Không tìm thấy xe!")
            return
    search_price = float(input("Nhập giá xe cần tìm: "))
    search_status = input("Nhập trạng thái: ")
    for cars in raw_cars:
        if search_price <= cars["rental_price"]:
            if search_status == "None":
                found = True
                print("Đã tìm thấy xe phù hợp!")
                return
            if search_status == "available" or search_status == "rented" or search_status == "mantenance":
                if search_status == cars["status"]:
                    found = True
