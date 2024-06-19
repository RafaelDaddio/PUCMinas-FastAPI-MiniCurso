from typing import List
from app.db.repositories import ClienteRepository
from app.db.repositories.models.cliente import Cliente
from app.modules.clientes.schemas import ClienteCreate, ClienteResponse
from app.utils.exceptions import RecursoNaoEncontradoException


class ClienteService():

    async def create(self, payload: ClienteCreate) -> ClienteResponse:
        # criar um objeto do tipo Cliente
        # cliente_criar = Cliente(nome = payload.nome,
        #                         cpf = payload.cpf,
        #                         ano_nascimento = payload.ano_nascimento)
        cliente_criar = Cliente(**payload.dict())        

        #invocar o metodo inserir desse Cliente
        cliente_criado = await cliente_criar.insert()

        return ClienteResponse.from_orm(cliente_criado)

        #retornar um ClienteResponse a partir do cliente criado
    
    async def get_all(self) -> List[ClienteResponse]:
        
        result = await ClienteRepository.get_all()
        response = [ClienteResponse.from_orm(cliente) for cliente in result]

        return response
    
    async def get_by_id(self, id:int) -> ClienteResponse:

        #recuperar o cliente
        cliente = await ClienteRepository.get_by_id(id)

        #se o cliente nao existe, lancar um erro
        if not cliente:
            raise RecursoNaoEncontradoException('Cliente nao encontrado.')

        #return cliente
        return ClienteResponse.from_orm(cliente)
