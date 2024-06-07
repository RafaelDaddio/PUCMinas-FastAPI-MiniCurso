from typing import List
from fastapi import APIRouter, HTTPException

from app.modules.cliente.schemas import ClienteCreate, ClienteResponse
from app.modules.cliente.services import ClienteService
from app.utils.exceptions import RecursoNaoEncontradoException


router = APIRouter()
service = ClienteService()


@router.post('/cliente', response_model=ClienteResponse, status_code=201)
async def create(payload: ClienteCreate):
    """
    Documentacao...
    """
    return await service.create(payload)


@router.get('/cliente', response_model=List[ClienteResponse], status_code=200)
async def get_all():
    """
    """
    return await service.get_all()


@router.get('/cliente/{id}', response_model=ClienteResponse, status_code=200)
async def get_by_id(id: int):
    """
    """
    try:
        return await service.get_by_id(id)
    except RecursoNaoEncontradoException as error:
        raise HTTPException(status_code=404, detail=str(error))