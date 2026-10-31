from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database import Base


class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    car_code = Column(String(10), unique= True, nullable= False)
    rental_price = Column(Float(10,2), nullable=False)
    car_type_id = Column(ForeignKey, Integer)

class CarsType(Base):
    __table_name__ = "cars_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable= False)