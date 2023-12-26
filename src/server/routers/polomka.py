import fastapi
from src.server.resolvers import polomka
from src.server.sql_base.models import Polomka

router = fastapi.APIRouter(prefix='/polomka', tags=['Polomka'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{polomka_id}', response_model=Polomka | dict)
def get(polomka_id: int) -> Polomka | dict:
    res = polomka.get(polomka_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Polomka] | dict)
def get_all() -> list[Polomka] | dict:
    return polomka.get_all()


@router.delete('/delete/{polomka_id}', response_model=str | dict)
def remove(polomka_id: int) -> str | dict:
    res = polomka.delete(polomka_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=Polomka | dict)
def create(new_polomka: Polomka) -> Polomka | dict:
    return polomka.create(new_polomka)


@router.put("/update/{polomka_id}", response_model=Polomka | dict)
def update(polomka_id: int, new_data: Polomka):
    return polomka.update(polomka_id=polomka_id,
                        new_data=new_data)