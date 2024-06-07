from typing import List

from app.db.engine import get_async_session
from .models.cliente import Cliente
from sqlalchemy import select


async def get_all() -> List[Cliente]:
    async with get_async_session() as session:
        instrucao = select(Cliente)
        print(instrucao)

        result = await session.execute(instrucao)

        return result.scalars().all()


async def get_by_id(id: int) -> Cliente | None:
    async with get_async_session() as session:
        instrucao = select(Cliente).where(Cliente.id == id)
        print(instrucao)

        result = await session.execute(instrucao)

        return result.scalars().one_or_none()