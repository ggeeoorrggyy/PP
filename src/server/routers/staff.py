import fastapi
from src.server.resolvers import staff
from src.server.sql_base.models import Staff

router = fastapi.APIRouter(prefix='/staff', tags=['Staff'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{staff_id}', response_model=Staff | dict)
def get(staff_id: int) -> Staff | dict:
    res = staff.get(staff_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Staff] | dict)
def get_all() -> list[Staff] | dict:
    return staff.get_all()


@router.delete('/delete/{staff_id}', response_model=str | dict)
def remove(staff_id: int) -> str | dict:
    res = staff.delete(staff_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=Staff | dict)
def create(new_staff: Staff) -> Staff | dict:
    return staff.create(new_staff)


@router.put("/update/{staff_id}", response_model=Staff | dict)
def update(staff_id: int, new_data: Staff):
    return staff.update(staff_id=staff_id,
                        new_data=new_data)