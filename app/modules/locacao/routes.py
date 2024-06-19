from fastapi import APIRouter, HTTPException

from app.modules.locacao.schemas import LocacaoCreate, LocacaoResponse
from app.modules.locacao.services import LocacaoService
from app.utils.exceptions import OperacaoInvalidaException, RecursoNaoEncontradoException


router = APIRouter()
service = LocacaoService()

@router.post('/locacao', response_model=LocacaoResponse, status_code=201)
async def aluga(payload: LocacaoCreate):
    """
    """
    try:
        return await service.aluga(payload)
    except RecursoNaoEncontradoException as error:
        raise HTTPException(status_code=404, detail=str(error))
    except OperacaoInvalidaException as error:
        raise HTTPException(status_code=422, detail=str(error))