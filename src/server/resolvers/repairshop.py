from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import CarRepairShop


def get(shop_id: int) -> CarRepairShop | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, City, Number, Name, Address, Service_id, Spare_parts_id, Staff_id FROM Car_repair_shop WHERE id=(?)',
        args=(shop_id,))

    return None if not res else CarRepairShop(
        id=res[0],
        City=res[1],
        Number=res[2],
        Name=res[3],
        Address=res[4],
        Service_id=res[5],
        Spare_parts_id=res[6],
        Staff_id=res[7]
    )


def get_all() -> list[CarRepairShop] | dict:
    shops_list = dbmanager.execute_query(
        query="SELECT id, City, Number, Name, Address, Service_id, Spare_parts_id, Staff_id FROM Car_repair_shop",
        fetchone=False)

    res = []

    if shops_list:
        for shop in shops_list:
            res.append(CarRepairShop(
                id=shop[0],
                City=shop[1],
                Number=shop[2],
                Name=shop[3],
                Address=shop[4],
                Service_id=shop[5],
                Spare_parts_id=shop[6],
                Staff_id=shop[7]
            ))

    return res


def delete(shop_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM Car_repair_shop WHERE id=(?) RETURNING id',
        args=(shop_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_shop: CarRepairShop) -> CarRepairShop | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO Car_repair_shop (City, Number, Name, Address, Service_id, Spare_parts_id, Staff_id VALUES (?, ?, ?) RETURNING id",
        args=(new_shop.City, new_shop.Number, new_shop.Name, new_shop.Address, new_shop.Service_id, new_shop.Spare_parts_id, new_shop.Staff_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(shop_id: int, new_data: CarRepairShop) -> CarRepairShop | dict:
    res = dbmanager.execute_query(
        query="UPDATE Car_repair_shop SET (City, Number, Name, Address. Service_id, Spare_parts_id, Staff_id) = (?, ?, ?) WHERE id=(?)",
        args=(new_data.City, new_data.Number, new_data.Name, new_data.Address, new_data.Service_id, new_data.Spare_parts, new_data.Staff_id, shop_id))

    if type(res) != dict:
        res = get(shop_id)

    return res