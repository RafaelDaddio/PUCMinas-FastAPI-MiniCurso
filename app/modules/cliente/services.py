from typing import List
from app.db.repositories.models.cliente import Cliente
from app.modules.cliente.schemas import ClienteCreate, ClienteResponse
from app.db.repositories import ClienteRepository
from app.utils.exceptions import RecursoNaoEncontradoException


class ClienteService():

    async def create(self, payload: ClienteCreate) -> ClienteResponse:

        # cliente_criar = Cliente(nome=payload.nome,
        #                         cpf=payload.cpf,
        #                         ano_nascimento = payload.ano_nascimento)
        
        cliente_criar = Cliente(**payload.dict())
        cliente_criado = await cliente_criar.insert()

        return ClienteResponse.from_orm(cliente_criado)
    
    async def get_all(self) -> List[ClienteResponse]:

        results = await ClienteRepository.get_all()

        return [ClienteResponse.from_orm(result) for result in results]
    
    async def get_by_id(self, id: int) -> ClienteResponse:

        result = await ClienteRepository.get_by_id(id)
        if not result:
            raise RecursoNaoEncontradoException("Recurso nao encontrado")
        
        return ClienteResponse.from_orm(result)

