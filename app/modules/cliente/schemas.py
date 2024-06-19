from app.utils.helpers import BaseSchema, MetaDatetimeSchema, docs_example


class ClienteCreate(BaseSchema):
    nome: str
    cpf: str
    ano_nascimento: int

    class Config:
        schema_extra = {
            'example': {
                'nome': 'Bilbo Baggins',
                'cpf': '111.111.111-11',
                'ano_nascimento': 2000
            }
        }

class ClienteUpdate(BaseSchema):
    nome: str | None
    cpf: str | None
    ano_nascimento: int | None
    saldo: float | None

    class Config:
        schema_extra = {
            'example': {
                'nome': 'Bilbo Baggins',
                'cpf': '111.111.111-11',
                'ano_nascimento': 2000,
                'saldo': 0.0
            }
        }

class ClienteResponse(ClienteCreate):
    id: int
    saldo: float

    metadatetime: MetaDatetimeSchema

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'nome': 'Bilbo Baggins',
                'cpf': '111.111.111-11',
                'ano_nascimento': 2000,
                'saldo': 0.0,
                'metadatetime': docs_example
            }
        }
