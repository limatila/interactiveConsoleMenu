from functools import wraps
from time import sleep
def exec(callback): #TODO: ver como importar o @exec de 'outrasFunctions.py'
    @wraps(callback)
    def wrapper(*args, **kwargs):
        print("...executando...")
        sleep(1)
        callback(*args, **kwargs)
    return wrapper

#Classe em si
class Calculadora:
    def __init__(self):
        self.contaTotal = 0

    @exec
    def soma(self, num1: int, num2: int) -> int:
        return num1 + num2
    @exec
    def subtracao(self, num1: int, num2: int) -> int:
        return num1 - num2
    
    @exec
    def conte_1(self) -> None:
        self.contaTotal += 1

        print(self.contaTotal) #Display

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.conte_1()
    print(calculadora.soma(3, 10))