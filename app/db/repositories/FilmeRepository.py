from typing import List

from app.db.engine import get_async_session
from .models.filme import Filme
from sqlalchemy import select


async def get_all() -> List[Filme]:
    async with get_async_session() as session:
        instrucao = select(Filme)
        print(instrucao)

        result = await session.execute(instrucao)

        return result.scalars().all()


async def get_by_id(id: int) -> Filme | None:
    async with get_async_session() as session:
        instrucao = select(Filme).where(Filme.id == id)
        print(instrucao)

        result = await session.execute(instrucao)

        return result.scalars().one_or_none()
