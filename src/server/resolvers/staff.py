from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Staff


def get(staff_id: int) -> Staff | None | dict:
    res = dbmanager.execute_query(
        query='SELECT Name, Surname, Patronymic, Date, Car_repair_shop, Post_id FROM staff WHERE id=(?)',
        args=(staff_id,))

    return None if not res else Staff(
        id=res[0],
        Name=res[1],
        Surname=res[2],
        Patronymic=res[3],
        Date=res[4],
        Car_repair_shop=res[5],
        Post_id=res[6]
    )


def get_all() -> list[Staff] | dict:
    staff_list = dbmanager.execute_query(
        query="SELECT id, Name, Surname, Patronymic, Date, Car_repair_shop, Post_id FROM staff",
        fetchone=False)

    res = []

    if staff_list:
        for staff in staff_list:
            res.append(Staff(
                id=staff[0],
                Name=staff[1],
                Surname=staff[2],
                Patronymic=staff[3],
                Date=staff[4],
                Car_repair_shop=staff[5],
                Post_id=staff[6]
            ))

    return res


def delete(staff_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM staff WHERE id=(?) RETURNING id',
        args=(staff_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_staff: Staff) -> Staff | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO staff (Name, Surname, patronymic, Date, Car_repair_shop, Post_id) VALUES (?, ?, ?, ?, ?, ?) RETURNING id",
        args=(new_staff.Name, new_staff.Surname, new_staff.Patronymic, new_staff.Date, new_staff.Car_repair_shop,
              new_staff.Post_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(staff_id: int, new_data: Staff) -> Staff | dict:
    res = dbmanager.execute_query(
        query="UPDATE staff SET (Name, Surname, Patronymic, Date, Car_repair_shop, Post_id) = (?, ?, ?, ?, ?, ?) WHERE id=(?)",
        args=(new_data.Name, new_data.Surname, new_data.Patronymic, new_data.Date, new_data.Car_repair_shop,
              new_data.Post_id, staff_id))

    if type(res) != dict:
        res = get(staff_id)

    return res