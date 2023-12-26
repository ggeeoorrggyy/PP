from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Car


def get(car_id: int) -> Car | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, Brand, Car_model, Year, Polomka_id, Service_id, Spare_parts_id FROM car WHERE id=(?)',
        args=(car_id,))

    return None if not res else Car(
        id=res[0],
        Brand=res[1],
        Car_model=res[2],
        Year=res[3],
        Polomka_id=res[4],
        Service_id=res[5],
        Spare_parts_id=res[6]
    )


def get_all() -> list[Car] | dict:
    car_list = dbmanager.execute_query(
        query="SELECT id, Brand, Car_model, Year, Polomka_id, Service_id, Spare_parts_id FROM car",
        fetchone=False)

    res = []

    if car_list:
        for car in car_list:
            res.append(Car(
                id=res[0],
                Brand=res[1],
                Car_model=res[2],
                Year=res[3],
                Polomka_id=res[4],
                Service_id=res[5],
                Spare_parts_id=res[6]
            ))

    return res


def delete(car_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM car WHERE id=(?) RETURNING id',
        args=(car_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_car: Car) -> Car | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO car (Brand, Car_model, Year, Polomka_id, Service_id, Spare_parts_id) VALUES (?, ?, ?) RETURNING id",
        args=(new_car.Brand, new_car.Car_model, new_car.Year, new_car.Polomka_id, new_car.Service_id, new_car.Spare_parts_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(car_id: int, new_data: Car) -> Car | dict:
    res = dbmanager.execute_query(
        query="UPDATE cars SET (Brand, Car_model, Year, Polomka_id, Service_id, Spare_parts_id) = (?, ?, ?) WHERE id=(?)",
        args=(new_data.Brand, new_data.Car_model, new_data.Year, new_data.Polomka_id, new_data.Service_id, new_data.Spare_parts_id, car_id))

    if type(res) != dict:
        res = get(car_id)

    return res