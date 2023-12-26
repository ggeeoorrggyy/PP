import fastapi
from src.server.resolvers import repairshop
from src.server.sql_base.models import CarRepairShop

router = fastapi.APIRouter(prefix='/shops', tags=['RepairShops'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{shop_id}', response_model=CarRepairShop | dict)
def get(shop_id: int) -> CarRepairShop | dict:
    res = repairshop.get(shop_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[CarRepairShop] | dict)
def get_all() -> list[CarRepairShop] | dict:
    return repairshop.get_all()


@router.delete('/delete/{shop_id}', response_model=str | dict)
def remove(shop_id: int) -> str | dict:
    res = repairshop.delete(shop_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=CarRepairShop | dict)
def create(new_shop: CarRepairShop) -> CarRepairShop | dict:
    return repairshop.create(new_shop)


@router.put("/update/{shop_id}", response_model=CarRepairShop | dict)
def update(shop_id: int, new_data: CarRepairShop):
    return repairshop.update(shop_id=shop_id,
                               new_data=new_data)