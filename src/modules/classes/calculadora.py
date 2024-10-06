class Calculadora:
    def __init__(self):
        self.contaTotal = 0

    def soma(self, num1, num2) -> int:
        return num1 + num2
    def subtracao(self, num1, num2) -> int:
        return num1 - num2
    
    def conte_1(self) -> None:
        self.contaTotal += 1

        print(self.contaTotal) #Display