from DataBase.db_init import DataBaseInit, DataBaseResponse
from DataBase.models import T
from structures import Level, Page, User
from sqlalchemy import select
from typing import Union


class Update(DataBaseInit):

    # обновление одной записи в определенную таблицу
    async def update(self, model: T, struct: Union[Level, Page, User]) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    query = await session.execute(select(model).where(model.id == struct.id))
                    record = query.scalar()
                    record.update_date(struct)
                    session.add(record)
                    await session.commit()
                    return DataBaseResponse(True, "Record update successfully")
                except Exception as e:
                    return DataBaseResponse(False, f"Error database update: -> {e}")


if __name__ == '__main__':
    print("Realisation class Update in database")
