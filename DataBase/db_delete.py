from typing import List
from DataBase.db_init import DataBaseInit, DataBaseResponse
from DataBase.models import T


class Delete(DataBaseInit):

    # Удаления одной записи в определенную таблицу
    async def delete(self, model: T) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    session.delete(model)
                    await session.commit()
                    return DataBaseResponse(True, "Record deleted successfully")
                except Exception as e:
                    return DataBaseResponse(False, f"Error database deleted: -> {e}")

    # Удаления списка записей одной транзакцией
    async def adds(self, models: List[T]) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    for model in models:
                        session.delete(model)
                    await session.commit()
                    return DataBaseResponse(True, "Records deleted successfully")
                except Exception as e:
                    return DataBaseResponse(False, f"Error database deleted: -> {e}")


if __name__ == '__main__':
    print("Realisation class Delete in database")
