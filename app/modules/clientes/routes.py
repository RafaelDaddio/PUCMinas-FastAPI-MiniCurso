from typing import List
from fastapi import APIRouter, HTTPException

from app.modules.clientes.schemas import ClienteCreate, ClienteResponse
from app.modules.clientes.services import ClienteService
from app.utils.exceptions import RecursoNaoEncontradoException


route = APIRouter()
service = ClienteService()

@route.post('/cliente', response_model=ClienteResponse, status_code=201)
async def create(payload: ClienteCreate):
    """
    """
    return await service.create(payload)

@route.get('/cliente', response_model=List[ClienteResponse], status_code=200)
async def get_all():
    """
    """
    return await service.get_all()

@route.get('/cliente/{id}', response_model=ClienteResponse, status_code=200)
async def get_by_id(id: int):
    """
    """
    try:
        return await service.get_by_id(id)
    except RecursoNaoEncontradoException as erro:
        raise HTTPException(status_code=404, detail=str(erro))
