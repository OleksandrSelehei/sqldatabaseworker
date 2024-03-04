from sqlalchemy.ext.asyncio.session import async_sessionmaker
from config import engine


# Иницилизация сессии с БД
class DataBaseInit:
    def __init__(self):
        self.engine = engine
        self.async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# Кастомная структура результата функции
class DataBaseResponse:
    def __init__(self, success: bool, data):
        self.success = success
        self.data = data
