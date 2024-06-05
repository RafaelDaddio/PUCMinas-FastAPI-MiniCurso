from app.utils.helpers import BaseSchema


class Operacao(BaseSchema):
    num1: float
    num2: float
    op: str

    class Config:
        schema_extra = {
            "example": {
                "num1": 4.5,
                "num2": 5.5,
                "op": "+"
            }
        }

class OperacaoResponse(BaseSchema):
    result: float

    class Config:
        schema_extra = {
            "example": {
                "result": 10
            }
        }
