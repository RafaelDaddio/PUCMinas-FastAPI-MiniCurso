from app.utils.helpers import BaseSchema, MetaDatetimeSchema, docs_example


class LocacaoCreate(BaseSchema):
    cliente_id: int
    filme_id: int
    duracao: int

    class Config:
        schema_extra = {
            'example': {
                'cliente_id': 1,
                'filme_id': 1,
                'duracao': 1
            }
        }


class LocacaoResponse(LocacaoCreate):
    id: int
    metadatetime: MetaDatetimeSchema

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'cliente_id': 1,
                'filme_id': 1,
                'duracao': 1,
                'metadatetime': docs_example
            }
        }