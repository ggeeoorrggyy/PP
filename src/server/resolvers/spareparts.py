from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Spareparts


def get(spares_id: int) -> Spareparts | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, Name, Price, Delivery_time, The_brand_of_the_car, Car_model FROM Spare_parts WHERE id=(?)',
        args=(spares_id,))

    return None if not res else Spareparts(
        id=res[0],
        Name=res[1],
        Price=res[2],
        Delivery_time=res[3],
        The_brand_of_the_car=res[4],
        Car_model=res[5]
    )


def get_all() -> list[Spareparts] | dict:
    Spares_list = dbmanager.execute_query(
        query="SELECT id, Name, Price, Delivery_time, The_brand_the_car, Car_model FROM Spare_parts",
        fetchone=False)

    res = []

    if Spares_list:
        for Spares in Spares_list:
            res.append(Spareparts(
                id=Spares[0],
                Name=Spares[1],
                Price=Spares[2],
                Delivery_time=Spares[3],
                The_brand_of_the_car=Spares[4],
                Car_model=Spares[5],

            ))

    return res


def delete(Spares_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM Spare_parts WHERE id=(?) RETURNING id',
        args=(Spares_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_spares: Spareparts) -> Spareparts | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO Spare_parts (Name, Price, Delivery_time, The_brand_the_car, Car_model) VALUES (?, ?, ?) RETURNING id",
        args=(new_spares.Name, new_spares.Price, new_spares.Delivery_time, new_spares.The_brand_the_car, new_spares.Car_model))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(spares_id: int, new_data: Spareparts) -> Spareparts | dict:
    res = dbmanager.execute_query(
        query="UPDATE Spare_parts SET (Name, Price, Delivery_time, The_brand_the_car, Car_model) = (?, ?, ?) WHERE id=(?)",
        args=(new_data.Name, new_data.Price, new_data.Delivery_time, new_data.The_brand_of_the_car, new_data.Car_model, spares_id))

    if type(res) != dict:
        res = get(spares_id)

    return res