from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Service


def get(service_id: int) -> Service | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, Name, Price, Time, Spare_parts_id FROM Service WHERE id=(?)',
        args=(service_id,))

    return None if not res else Service(
        id=res[0],
        Name=res[1],
        Price=res[2],
        Time=res[3],
        Spare_parts_id=res[4]
    )


def get_all() -> list[Service] | dict:
    service_list = dbmanager.execute_query(
        query="SELECT id, Name, Price, Time, Spare_parts_id FROM service",
        fetchone=False)

    res = []

    if service_list:
        for service in service_list:
            res.append(Service(
                id=service[0],
                Name=service[1],
                Price=service[2],
                Time=service[3],
                Spare_parts_id=service[4]
            ))

    return res


def delete(service_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM service WHERE id=(?) RETURNING id',
        args=(service_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_service: Service) -> Service | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO Service (Name, Price, Time, Spare_parts_id) VALUES (?, ?) RETURNING id",
        args=(new_service.Name, new_service.Price, new_service.Time, new_service.Spare_parts_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(service_id: int, new_data: Service) -> Service | dict:
    res = dbmanager.execute_query(
        query="UPDATE Service SET (Name, Price, Time, Spare_parts_id) = (?, ?) WHERE id=(?)",
        args=(new_data.Name, new_data.Price, new_data.Time, new_data.Spare_parts_id, service_id))

    if type(res) != dict:
        res = get(service_id)

    return res