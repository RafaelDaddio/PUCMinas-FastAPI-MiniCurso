from app.db.repositories import ClienteRepository, FilmeRepository
from app.db.repositories.models.locacao import Locacao
from app.modules.locacao.schemas import LocacaoCreate, LocacaoResponse
from app.utils.exceptions import OperacaoInvalidaException, RecursoNaoEncontradoException


class LocacaoService():

    async def aluga(self, payload: LocacaoCreate) -> LocacaoResponse:

        # checar se cliente e filme existem
        cliente = await ClienteRepository.get_by_id(payload.cliente_id)
        if not cliente:
            raise RecursoNaoEncontradoException("Cliente nao existe")
        
        filme = await FilmeRepository.get_by_id(payload.filme_id)
        if not filme:
            raise RecursoNaoEncontradoException("Filme nao existe")

        # checar filme alugado
        if filme.alugado:
            raise OperacaoInvalidaException("Filme esta alugado")

        # checar saldo cliente
        if cliente.saldo < filme.preco * payload.duracao:
            raise OperacaoInvalidaException("Saldo insuficiente")

        # alugar > colocar o filme como indisponivel, atualizar saldo, inserir locacao
        await filme.update(alugado = True)
        await cliente.update(saldo = cliente.saldo - filme.preco * payload.duracao)

        locacao = Locacao(**payload.dict())
        locacao_criado = await locacao.insert()

        return LocacaoResponse.from_orm(locacao_criado)
