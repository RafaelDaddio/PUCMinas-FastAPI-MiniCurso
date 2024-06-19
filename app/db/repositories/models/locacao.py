from app.db.base import BaseMixin
from app.db.engine import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class Locacao(Base, BaseMixin):
    __tablename__ = 'locacao'

    cliente_id: Mapped[int] = mapped_column(ForeignKey('cliente.id'))
    filme_id: Mapped[int] = mapped_column(ForeignKey('filme.id'))
    duracao: Mapped[int]