from app.db.base import BaseMixin
from app.db.engine import Base

from sqlalchemy.orm import Mapped, mapped_column

class Filme(Base, BaseMixin):
    __tablename__ = 'filme'

    nome: Mapped[str]
    ano_lancamento: Mapped[int]
    duracao: Mapped[int]
    preco: Mapped[float]
    alugado: Mapped[bool] = mapped_column(default=False)