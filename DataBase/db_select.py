from typing import Type
from sqlalchemy import select
from .models import T
from DataBase.db_init import DataBaseInit, DataBaseResponse
from structures import FilterLog
from datetime import datetime


class Select(DataBaseInit):
    # Получения всех записей
    async def all(self, model: Type[T]) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    query = await session.execute(select(model))
                    records = query.scalars().all()
                    return DataBaseResponse(True, records)
                except Exception as e:
                    return DataBaseResponse(False, e)

    async def all_renge(self, model: Type[T], slice_range: int) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    query = await session.execute(select(model))
                    records = query.scalars().all()
                    if len(records) > slice_range:
                        records = records[-slice_range:]
                    return DataBaseResponse(True, records)
                except Exception as e:
                    return DataBaseResponse(False, e)

    async def filter_log(self, model: Type[T], params: FilterLog) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    query = select(model)
                    if params.nickname is not None and params.nickname != "":
                        query = query.filter(model.user_name == params.nickname)

                    if params.right is not None and params.right != "":
                        query = query.filter(model.rights == int(params.right))

                    if params.start_date is not None and params.start_date != "":
                        query = query.filter(model.date >= datetime.strptime(params.start_date, "%Y-%m-%d"))

                    if params.end_date is not None and params.end_date != "":
                        query = query.filter(model.date <= datetime.strptime(params.end_date, "%Y-%m-%d"))
                    results = await session.execute(query)
                    records = results.scalars().all()
                    if params.quantity is not None and params.quantity != "":
                        if len(records) > int(params.quantity):
                            records = records[-int(params.quantity):]
                    return DataBaseResponse(True, records)
                except Exception as e:
                    return DataBaseResponse(False, e)

    # Получения записи по ID
    async def by_id(self, model: Type[T], id: int) -> DataBaseResponse:
        async with self.engine.connect() as conn:
            async with self.async_session_maker(bind=conn) as session:
                try:
                    query = await session.execute(select(model).where(model.id == id))
                    record = query.scalar()
                    return DataBaseResponse(True, record)
                except Exception as e:
                    return DataBaseResponse(False, e)


if __name__ == "__main__":
    print("Realisation class Select in database")
