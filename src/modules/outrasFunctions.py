def say_hi(nome, age):
    print(f"Olá {nome}, que legal que você tem {age} anos!")

def faca_isso() -> str:
    return 'isso'

def faca_aquilo() -> str:
    return 'aquilo'

contaTotal: int = 0
def conte_1() -> int:
    global contaTotal
    contaTotal += 1

    return contaTotal #Display