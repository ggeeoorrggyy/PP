import sqlite3
import os
from setting import DB_PATH


class DbManager:
    def __init__(self, db_path: str):  # Функция инициализации класа добавление изначальных параметров
        self.db_path = db_path

    def connect_db(self) -> tuple[sqlite3.Connection, sqlite3.Cursor]:  # Функция создание полключения и курсора
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        return connect, cursor

    def create_db(self, create_script: str) -> None:  # Функция создание базы данных если база данных  уже создана функция не отработает
        if not os.path.exists(self.db_path):
            self.execute_sql_script(create_script)

    def execute_sql_script(self, script: str) -> None:  # Функция выполнения скрипта
        connect, cursor = self.connect_db()
        cursor.executescript(open(script).read())
        connect.commit()
        connect.close()

    def execute_query(self, query: str, fetchone: bool = True, args: tuple = None):  # Функция выполния запроса и выборки по всем данным таблицы и присвоение переменной args тип даных кортеж и значение картежа по умолчанию None
        connect, cursor, = self.connect_db()

        try:  # Если fethone try то выполниться запрос на определенную строку таблицы иначе выполнятся запрос по всей таблицы
            if fetchone:
                res = cursor.execute(query, args).fetchone()
            else:
                res = cursor.execute(query).fetchall()
        except sqlite3.IntegrityError:  # Обработка иключений точнее ошибок
            connect.close()
            return {'error': 'request contains unique error'}

        connect.commit()
        connect.close()
        return res


dbmanager = DbManager(db_path=DB_PATH)