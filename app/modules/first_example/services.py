from app.modules.first_example.schemas import Operacao, OperacaoResponse
from app.utils.exceptions import DivisaoPorZeroException, OperacaoInvalidaException


class FirstExampleService():

    def calcula(self, payload: Operacao):
        num1, num2, op = payload.num1, payload.num2, payload.op

        match op:
            case '+': result = num1 + num2
            case '-': result = num1 - num2
            case '*': result = num1 * num2
            case '/': 
                if num2 == 0:
                    raise DivisaoPorZeroException("Impossivel dividir por zero!")
                result = num1 / num2
            case _: raise OperacaoInvalidaException("Essa operação é invalida!")
        
        return OperacaoResponse(result=result)