import sqlite3
from settings import Settings


settings = Settings()

def get_db_connecttion() -> sqlite3.Connection:
    return sqlite3.connect(settings.sqlite_db_name)