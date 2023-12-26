from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Order


def get(order_id: int) -> Order | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, Name_order, Name_of_service, Car_repair_shop_id, Spare_parts_id, Staff_id FROM order WHERE id=(?)',
        args=(order_id,))

    return None if not res else Order(
        id=res[0],
        Name_order=res[1],
        Name_of_service=res[2],
        Car_repair_shop_id=res[3],
        Spare_parts_id=res[4],
        Staff_id=res[5]
    )


def get_all() -> list[Order] | dict:
    order_list = dbmanager.execute_query(
        query="SELECT id, Name_order, Name_of_service, Car_repair_shop_id, Spare_parts_id, Staff_id FROM order",
        fetchone=False)

    res = []

    if order_list:
        for order in order_list:
            res.append(Order(
                id=order[0],
                Name_order=order[1],
                Name_of_service=order[2],
                Car_repair_shop_id=order[3],
                Spare_parts_id=order[4],
                Staff_id=order[5]
            ))

    return res


def delete(order_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM order WHERE id=(?) RETURNING id',
        args=(order_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_order: Order) -> Order | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO Order (Name_order, Name_of_service, Car_repair_shop_id, Spare_parts_id, Staff_id) VALUES (?, ?) RETURNING id",
        args=(new_order.Name_order, new_order.Name_of_service, new_order.Car_repair_shop_id, new_order.Spare_parts_id, new_order.Staff_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(order_id: int, new_data: Order) -> Order | dict:
    res = dbmanager.execute_query(
        query="UPDATE order SET (Name_order, Name_of_service, Car_repair_shop_id, Spare_parts_id, Staff_id) = (?, ?) WHERE id=(?)",
        args=(new_data.Name_order, new_data.Car_repair_shop_id, new_data.Spare_parts_id, new_data.Staff_id, order_id))

    if type(res) != dict:
        res = get(order_id)

    return res