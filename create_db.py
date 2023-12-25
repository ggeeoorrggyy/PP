from src.server.sql_base.db_manager import dbmanager
from settings import SQL_SCRIPTS_DIR


dbmanager.create_db(f"{SQL_SCRIPTS_DIR}/tables.sql")