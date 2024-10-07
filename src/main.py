# Principal conceito do Menu: repetir enquanto o usuário não parar sua execução.
# O menu (o programa inteiro) se fecha apenas quando o usuário não necessita mais dele.

#Importando funções de exemplo
from modules import outrasFunctions
from modules.submenus import complexMenus
import time

def main():
    nomeInserido = str(input("\nOlá usuário, informe o seu nome porfavor\t->"))
    print(f"\nBem vindo ao Menu, {nomeInserido.split(" ")[0]}!")

    #Execução Principal:
    UsuarioSaiu = False
    while UsuarioSaiu == False:
        time.sleep(1.2)
        #Passo 1: Mostrando o Menu a cada tentativa
        print("\n*                                                  \
              \n---Menu Principal---                                \
              \nEscolha uma das opções listadas abaixo, por número: \
              \n*                                                   \
              \n\n---Opções:---                                     \
              \n1 - Faça isso                                       \
              \n2 - Faça aquilo                                     \
              \n3 - Dizer Olá                                       \
              \n4 - Cálculos                                        \
              \n5 - SAIR \n")
    
        time.sleep(0.5)
        #Passo 2: pedindo que o usuário escolha uma opção
        try:
            escolha = int(input("\nEscolha uma opção (disponíveis de 1 a 5)\t->").split(" ")[0])
        except ValueError:
            print("\nOpção inválida. Selecione de 1 a 5, apenas digitando o algarismo.")
            continue


        #Passo 3: executando a opção escolhida por ele
        match(escolha):
            case 1:
                outrasFunctions.faca_isso()
                break;
            case 2:
                outrasFunctions.faca_aquilo()
                break;
            case 3:
                idadeInserida = int(input("Quantos anos você tem?\t->"))  #filtra apenas o número
                outrasFunctions.print_ola(nomeInserido, idadeInserida)
                break;
            case 4:
                complexMenus.menuCalculadora(nomeInserido) #Pula para execução do SubMenu
                break;
            case 5: 
                print("Até mais!")
                time.sleep(1.5)
                UsuarioSaiu = True  #* O usuário Opta por SAIR, encerrando o programa.
                break;
            case _:
                print("Option Error: Opção não existe, voltando...")
        
        #Após execução de algo, o programa vai se repetir.
        print("Voltando ao Menu...")
        # continue no loop...


if __name__ == '__main__':
    print("Programa de @Átila Lima, 2024.")
    main()
    print("Obrigado por usar o Menu!")