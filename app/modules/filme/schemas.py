from app.utils.helpers import BaseSchema, MetaDatetimeSchema, docs_example


class FilmeCreate(BaseSchema):
    nome: str
    ano_lancamento: int
    duracao: int
    preco: float

    class Config:
        schema_extra = {
            'example': {
                'nome': 'O Senhor dos Aneis: Sociedade do Anel',
                'ano_lancamento': 2001,
                'duracao': 178,
                'preco': 10.50
            }
        }


class FilmeResponse(FilmeCreate):
    id: int
    alugado: bool
    metadatetime: MetaDatetimeSchema

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'nome': 'O Senhor dos Aneis: Sociedade do Anel',
                'ano_lancamento': 2001,
                'duracao': 178,
                'preco': 10.50,
                'alugado': False,
                'metadatetime': docs_example
            }
        }
