from typing import List
from fastapi import APIRouter, HTTPException

from app.modules.filme.schemas import FilmeCreate, FilmeResponse
from app.modules.filme.services import FilmeService
from app.utils.exceptions import RecursoNaoEncontradoException


router = APIRouter()
service = FilmeService()


@router.post('/filme', response_model=FilmeResponse, status_code=201)
async def create(payload: FilmeCreate):
    """
    ## Cria um filme.

    ### Argumentos:
     > payload (FilmeCreate)  

    ### Retorna:
     > FilmeResponse  
    """
    return await service.create(payload)


@router.get('/filme', response_model=List[FilmeResponse], status_code=200)
async def get_all():
    """
    ## Recupera todos os filmes.

    ### Retorna:
     > List[FilmeResponse]
    """
    return await service.get_all()


@router.get('/filme/{id}', response_model=FilmeResponse, status_code=200)
async def get_by_id(id: int):
    """
    ## Recupera um filme por id.

    ### Argumentos:
     > id (int)   

    ### Retorna:
     > FilmeResponse

    ### Exceções:
     > Código 404: caso o filme nao exista.
    """
    try:
        return await service.get_by_id(id)
    except RecursoNaoEncontradoException as error:
        raise HTTPException(status_code=404, detail=str(error))