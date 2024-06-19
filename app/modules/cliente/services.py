from typing import List
from app.db.repositories.models.cliente import Cliente
from app.modules.cliente.schemas import ClienteCreate, ClienteResponse, ClienteUpdate
from app.db.repositories import ClienteRepository
from app.utils.exceptions import OperacaoInvalidaException, RecursoNaoEncontradoException


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
            raise RecursoNaoEncontradoException("Cliente nao encontrado")
        
        return ClienteResponse.from_orm(result)
    
    async def delete_by_id(self, id: int) -> ClienteResponse:

        result = await ClienteRepository.get_by_id(id)
        if not result:
            raise RecursoNaoEncontradoException("Cliente nao encontrado")
        
        await result.delete()

        return ClienteResponse.from_orm(result)
    
    async def update_by_id(self, id: int, payload: ClienteUpdate):

        result = await ClienteRepository.get_by_id(id)
        if not result:
            raise RecursoNaoEncontradoException("Cliente nao encontrado")
        
        if payload.saldo and payload.saldo < 0:
            raise OperacaoInvalidaException("Saldo invalido")
        
        result_updated = await result.update(**payload.dict(exclude_none=True))

        return ClienteResponse.from_orm(result_updated)
        

