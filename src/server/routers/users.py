from fastapi import APIRouter
from src.server.sql_base.models import User, UserReg
from src.server.resolvers import user


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/login", response_model=dict)
def checking_login(user: User) -> dict:
    power_level = user.check_login(user)
    print(power_level)
    if type(power_level) == tuple:
        return {"code": 200, "message": "login correct", "position_id": power_level}
    else:
        return {"code": 400, "message": "login incorrect", "position_id": None}


@router.post("/register", response_model=int | dict)
def reg_user(user: UserReg) -> int | dict:
    return user.register(user)