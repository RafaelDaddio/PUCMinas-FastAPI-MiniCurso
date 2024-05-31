from app.modules.first_example.schemas import Operacao, OperacaoResponse
from app.utils.exceptions import DivisaoPorZeroException, SinalInvalidoException


class FirstExampleService():

    def calcula(self, payload: Operacao):
        num1, num2, sinal = payload.num1, payload.num2, payload.sinal

        match sinal:
            case '+': result = num1 + num2
            case '-': result = num1 - num2
            case '*': result = num1 * num2
            case '/':
                if num2 == 0:
                    raise DivisaoPorZeroException("Impossível dividir por zero!")
                result = num1 / num2
            case _: raise SinalInvalidoException("Sinal Inválido")

        return OperacaoResponse(result=result)
