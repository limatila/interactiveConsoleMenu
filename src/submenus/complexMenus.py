from modules.classes.calculadora import Calculadora #! Não funcionando

def menuCalculadora(nome) -> None:
    print(f"\n--Entendido {nome}. Abrindo Calculadora...")

    calc = Calculadora()

    calculadoraFechou = False
    while calculadoraFechou == False:
        print("\n---Menu da Calculadora---                           \
        \n\n---Opções---                                      \
        \n1 - Soma                                            \
        \n2 - Subtração                                       \
        \n3 - Conte a partir de 1                             \
        \n4 - Voltar ao Menu \n")
        
        try:
            escolhaCalculadora = int(input("Escolha uma opção (disponíveis de 1 a 4)\t->").split(" ")[0])
        except ValueError:
            print("\nOpção inválida. Selecione de 1 a 4, apenas digitando o algarismo.")
        
        
        match(escolhaCalculadora):
            case 1:
                numero1 = int(input("Insira o primeiro número: "))
                numero2 = int(input("Insira o segundo número: "))
                print("A Soma desses dois números é", calc.soma())
                break;
            case 2:
                numero1 = int(input("Insira o primeiro número: "))
                numero2 = int(input("Insira o segundo número: "))
                print("A Subtração desses dois números é", calc.soma())
                break;
            case 3:
                calc.conte_1()
                break;
            case 4:
                print("Voltando ao Menu Principal...")
                calculadoraFechou = True
            case _:
                print("Option Error: Opção não existe, voltando...")