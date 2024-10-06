from functools import wraps
from time import sleep

def exec(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        print("...executando...")
        sleep(1)
        callback(*args, **kwargs)
    return wrapper

@exec
def print_ola(nome, age) -> None:
    print(f"Olá {nome}, que legal que você tem {age} anos!")

@exec
def faca_isso() -> None:
    print('feito isso')

@exec
def faca_aquilo() -> None:
    print('feito aquilo')

contaTotal: int = 0
def conte_1() -> None:
    global contaTotal
    contaTotal += 1
    
    print(contaTotal) #Display

#Testing manually
if __name__ == '__main__':
    print_ola('Joaquim', 20)
    faca_isso()
    faca_aquilo()
    conte_1()