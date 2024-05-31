from fastapi import APIRouter, HTTPException

from app.modules.first_example.schemas import Operacao, OperacaoResponse
from app.modules.first_example.services import FirstExampleService
from app.utils.exceptions import DivisaoPorZeroException, SinalInvalidoException


route = APIRouter()
service = FirstExampleService()


@route.get("/hello", response_model=str, status_code=200)
async def hello_world():
    """
    ## Diz oi!

    """
    return "Hello world!"


@route.post("/calcula", response_model=OperacaoResponse, status_code=201)
async def calcula(payload: Operacao):
    """
    ## Calcula uma operação entre dois numeros.

    ### Args:
     > num1 (float)  
     > num2 (float)  
     > sinal (str)

    ### Raises:
     > HTTPException: lança um erro 422 se o sinal eh invalido ou 409 se for divisao por zero.

    ### Retorna:
     > resultado (float)
    """
    try:
        return service.calcula(payload)
    except SinalInvalidoException as erro:
        raise HTTPException(status_code=422, detail=str(erro))
    except DivisaoPorZeroException as erro:
        raise HTTPException(status_code=409, detail=str(erro))
