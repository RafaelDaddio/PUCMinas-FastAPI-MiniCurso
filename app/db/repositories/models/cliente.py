from app.db.base import BaseMixin
from app.db.engine import Base

from sqlalchemy.orm import Mapped, mapped_column

class Cliente(Base, BaseMixin):
    __tablename__ = 'cliente'

    nome: Mapped[str]
    cpf: Mapped[str]
    ano_nascimento: Mapped[int]
    saldo: Mapped[float] = mapped_column(default=0)