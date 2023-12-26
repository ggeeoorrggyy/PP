from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Polomka


def get(polomka_id: int) -> Polomka | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, name_of_polomka FROM polomka WHERE id=(?)',
        args=(polomka_id,))

    return None if not res else Polomka(
        id=res[0],
        name_of_polomka=res[1],
    )


def get_all() -> list[Polomka] | dict:
    polomka_list = dbmanager.execute_query(
        query="SELECT id, name_of_polomka FROM polomka",
        fetchone=False)

    res = []

    if polomka_list:
        for polomka in polomka_list:
            res.append(Polomka(
                id=polomka[0],
                name_of_polomka=polomka[1],
            ))

    return res


def delete(polomka_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM polomka WHERE id=(?) RETURNING id',
        args=(polomka_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_polomka: Polomka) -> Polomka | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO polomka (name_of_polomka) VALUES (?, ?) RETURNING id",
        args=(new_polomka.name_of_polomka))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(polomka_id: int, new_data: Polomka) -> Polomka | dict:
    res = dbmanager.execute_query(
        query="UPDATE polomka SET (name_of_polomka) = (?, ?) WHERE id=(?)",
        args=(new_data.name_of_polomka, polomka_id))

    if type(res) != dict:
        res = get(polomka_id)

    return res