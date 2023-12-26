import fastapi
from src.server.resolvers import car
from src.server.sql_base.models import Car

router = fastapi.APIRouter(prefix='/car', tags=['Car'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{car_id}', response_model=Car | dict)
def get(car_id: int) -> Car | dict:
    res = car.get(car_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Car] | dict)
def get_all() -> list[Car] | dict:
    return car.get_all()


@router.delete('/delete/{car_id}', response_model=str | dict)
def remove(car_id: int) -> str | dict:
    res = car.delete(car_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=Car | dict)
def create(new_car: Car) -> Car | dict:
    return car.create(new_car)


@router.put("/update/{car_id}", response_model=Car | dict)
def update(car_id: int, new_data: Car):
    return car.update(car_id=car_id,
                       new_data=new_data)