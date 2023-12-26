from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import User, UserReg


def check_login(user: User) -> int | dict:
    return dbmanager.execute_query(query="SELECT power_level FROM users WHERE (login, password) = (?, ?)",
                                   args=(user.login, user.password))


def register(user: UserReg) -> int | dict:
    return dbmanager.execute_query(query="INSERT INTO users(login, password, power_level)"
                                         "VALUES (?, ?, ?)"
                                         "RETURNING id",
                                   args=(user.login, user.password, user.power_level))[0]