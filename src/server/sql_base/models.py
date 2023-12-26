from typing import Optional
from pydantic import BaseModel


class BaseModelModify(BaseModel):
    id: Optional[int]


class Car(BaseModelModify):
    Brand: str
    Car_model: str
    Year: str
    Polomka_id: int
    Service_id: int
    Spare_parts_id: int


class CarRepairShop(BaseModelModify):
    City: str
    Number: str
    Name: str
    Address: str
    Service_id: int
    Spare_parts: int
    Stuff_id: int

class Staff(BaseModelModify):
    Name: str
    Surname: str
    Patronymic: str
    Date: int
    Car_repair_shop: str
    Post_id: int


class Post(BaseModelModify):
    Name_post: str


class Polomka(BaseModelModify):
    Name_of_polomka: str


class Spareparts(BaseModelModify):
    Name: str
    Price: str
    Delivery_time: str
    The_brand_of_the_car: str
    Car_model: str

class Service(BaseModelModify):
    Name: str
    Price: str
    Time: int
    Spare_parts_id: int

class Order(BaseModelModify):
    Name_order: str
    Name_of_service: str
    Car_repair_shop_id: int
    Spare_parts_id: int
    Staff_id: int


class User(BaseModelModify):
    login: str
    password: str


class UserReg(User):
    power_level: int