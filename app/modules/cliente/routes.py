from typing import List
from fastapi import APIRouter, HTTPException

from app.modules.cliente.schemas import ClienteCreate, ClienteResponse, ClienteUpdate
from app.modules.cliente.services import ClienteService
from app.utils.exceptions import OperacaoInvalidaException, RecursoNaoEncontradoException


router = APIRouter()
service = ClienteService()


@router.post('/cliente', response_model=ClienteResponse, status_code=201)
async def create(payload: ClienteCreate):
    """
    ## Cria um cliente.

    ### Argumentos:
     > payload (ClienteCreate)  

    ### Retorna:
     > ClienteResponse  
    """
    return await service.create(payload)


@router.get('/cliente', response_model=List[ClienteResponse], status_code=200)
async def get_all():
    """
    ## Recupera todos os clientes.

    ### Retorna:
     > List[ClienteResponse]
    """
    return await service.get_all()


@router.get('/cliente/{id}', response_model=ClienteResponse, status_code=200)
async def get_by_id(id: int):
    """
    ## Recupera um cliente por id.

    ### Argumentos:
     > id (int)   

    ### Retorna:
     > ClienteResponse

    ### Exceções:
     > Código 404: caso o cliente nao exista.
    """
    try:
        return await service.get_by_id(id)
    except RecursoNaoEncontradoException as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.delete('/cliente/{id}', response_model=ClienteResponse, status_code=200)
async def delete_by_id(id: int):
    """
    """
    try:
        return await service.delete_by_id(id)
    except RecursoNaoEncontradoException as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.patch('/cliente/{id}', response_model=ClienteResponse, status_code=200)
async def update_by_id(id:int , payload: ClienteUpdate):
    """
    """
    try:
        return await service.update_by_id(id, payload)
    except RecursoNaoEncontradoException as error:
        raise HTTPException(status_code=404, detail=str(error))
    except OperacaoInvalidaException as error:
        raise HTTPException(status_code=422, detail=str(error))
    