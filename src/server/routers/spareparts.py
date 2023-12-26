import fastapi
from src.server.resolvers import spareparts
from src.server.sql_base.models import Spareparts

router = fastapi.APIRouter(prefix='/spareparts', tags=['Spareparts'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{spareparts_id}', response_model=Spareparts | dict)
def get(spareparts_id: int) -> Spareparts | dict:
    res = spareparts.get(spareparts_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Spareparts] | dict)
def get_all() -> list[Spareparts] | dict:
    return spareparts.get_all()


@router.delete('/delete/{spareparts_id}', response_model=str | dict)
def remove(spareparts_id: int) -> str | dict:
    res = spareparts.delete(spareparts_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=Spareparts | dict)
def create(new_spareparts: Spareparts) -> Spareparts | dict:
    return spareparts.create(new_spareparts)


@router.put("/update/{spareparts_id}", response_model=Spareparts | dict)
def update(spareparts_id: int, new_data: Spareparts):
    return spareparts.update(spareparts_id=spareparts_id,
                        new_data=new_data)