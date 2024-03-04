from typing import List
from DataBase.db_init import DataBaseInit, DataBaseResponse
from DataBase.models import T


class Insert(DataBaseInit):

    # Добовления одной записи в определенную таблицу
    async def add(self, model: T) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    session.add(model)
                    await session.commit()
                    return DataBaseResponse(True, "Record added successfully")
                except Exception as e:
                    return DataBaseResponse(False, f"Error database insert: -> {e}")

    # Добавления списка записей одной транзакцией
    async def adds(self, models: List[T]) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    for model in models:
                        session.add(model)
                    await session.commit()
                    return DataBaseResponse(True, "Records added successfully")
                except Exception as e:
                    return DataBaseResponse(False, f"Error database insert: -> {e}")


if __name__ == '__main__':
    print("Realisation class Insert in database")
