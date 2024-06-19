from typing import List
from app.db.engine import get_async_session
from app.db.repositories.models.cliente import Cliente

from sqlalchemy import select


async def get_all() -> List[Cliente]:
    async with get_async_session() as session:
        operacao = select(Cliente)
        print(operacao)

        result = await session.execute(operacao)

        return result.scalars().all()
    

async def get_by_id(id: int) -> Cliente | None:
    async with get_async_session() as session:
        operacao = select(Cliente).where(Cliente.id == id)
        result = await session.execute(operacao)

        return result.scalars().one_or_none()
        
