import fastapi
from src.server.resolvers import order
from src.server.sql_base.models import Order

router = fastapi.APIRouter(prefix='/order', tags=['Order'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{order_id}', response_model=Order | dict)
def get(order_id: int) -> Order | dict:
    res = order.get(order_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Order] | dict)
def get_all() -> list[Order] | dict:
    return Order.get_all()


@router.delete('/delete/{order_id}', response_model=str | dict)
def remove(order_id: int) -> str | dict:
    res = order.delete(order_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=Order | dict)
def create(new_order: Order) -> Order | dict:
    return order.create(new_order)


@router.put("/update/{order_id}", response_model=Order | dict)
def update(order_id: int, new_data: Order):
    return order.update(order_id=order_id,
                               new_data=new_data)