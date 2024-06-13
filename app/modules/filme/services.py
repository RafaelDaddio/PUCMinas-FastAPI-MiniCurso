from typing import List
from app.db.repositories.models.filme import Filme
from app.modules.filme.schemas import FilmeCreate, FilmeResponse
from app.db.repositories import FilmeRepository
from app.utils.exceptions import RecursoNaoEncontradoException


class FilmeService():

    async def create(self, payload: FilmeCreate) -> FilmeResponse:
        
        filme_criar = Filme(**payload.dict())
        filme_criado = await filme_criar.insert()

        return FilmeResponse.from_orm(filme_criado)
    
    async def get_all(self) -> List[FilmeResponse]:

        results = await FilmeRepository.get_all()

        return [FilmeResponse.from_orm(result) for result in results]
    
    async def get_by_id(self, id: int) -> FilmeResponse:

        result = await FilmeRepository.get_by_id(id)
        if not result:
            raise RecursoNaoEncontradoException("Recurso nao encontrado")
        
        return FilmeResponse.from_orm(result)

