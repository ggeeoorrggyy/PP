import fastapi
from src.server.resolvers import service
from src.server.sql_base.models import Service

router = fastapi.APIRouter(prefix='/service', tags=['Service'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{service_id}', response_model=Service | dict)
def get(service_id: int) -> Service | dict:
    res = service.get(service_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Service] | dict)
def get_all() -> list[Service] | dict:
    return service.get_all()


@router.delete('/delete/{service_id}', response_model=str | dict)
def remove(service_id: int) -> str | dict:
    res = service.delete(service_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=Service | dict)
def create(new_service: Service) -> Service | dict:
    return service.create(new_service)


@router.put("/update/{service_id}", response_model=Service | dict)
def update(service_id: int, new_data: Service):
    return service.update(service_id=service_id,
                        new_data=new_data)