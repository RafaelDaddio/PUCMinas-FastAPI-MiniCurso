from fastapi import APIRouter, HTTPException

from app.modules.first_example.schemas import Operacao, OperacaoResponse
from app.modules.first_example.services import FirstExampleService
from app.utils.exceptions import DivisaoPorZeroException, OperacaoInvalidaException


route = APIRouter()
service = FirstExampleService()

@route.get("/ola", response_model=str, status_code=200)
async def hello_world():
    """
    ## Diz oi!
    """
    return "Hello World"

@route.post("/calculadora", response_model=OperacaoResponse, status_code=201)
async def calculadora(payload: Operacao):
    """
    ## Calcula uma operação entre dois numeros.

    ### Argumentos:
     > num1 (float)  
     > num2 (float)  
     > op (str)  

    ### Retorna:
     > resultado (float)

    ### Exceções:
     > Código 422: caso a operação seja inválida.  
     > Código 409: caso ocorra divisão por zero.
    """
    try:
        return service.calcula(payload)
    except OperacaoInvalidaException as erro:
        raise HTTPException(status_code=422, detail=str(erro))
    except DivisaoPorZeroException as erro:
        raise HTTPException(status_code=409, detail=str(erro))
