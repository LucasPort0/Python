'''
Escreva o jogo dos 15 (dos números). Utilize as funções escritas
em aula e mais três feitas agora:
    1 - VerificaSeVenceu: Recebe uma matriz 4x4 e verifica se os números estão
    ordenados de forma que o jogador venceu
    2 - VerificaJogada: Verifica se a jogada escolhida pelo usuário é válida
    3 - ImprimeJogo: Função que imprime o jogo na tela do usuário
Você pode fazer quantas funções adcionais quanto quiser

Organize o seu jogo dentro da função main. Dê para o usuário a toda rodada
a opção de desistir(0) ou de inserir uma posição(1), a posição inserida
será feita colocando a linha e coluna da matriz, por exemplo 11 significa que
estamos nos referenciando ao elemento da linha 1 coluna 1, 32 se referencia ao
elemento da linha 3 coluna 2

2) Escreva uma função recursiva que retorna a soma de n até zero

By Lucas Porto
Treinamento Linguagem Python
27/10/2021
'''
import random

def main():
    '''
    Função principal de execução do programa
    '''
    Jogo = ConstruirMatriz()
    while True:
        ImprimeJogo(Jogo)
        #o usuário ira decidir se quer trocar a posição dos elementos da matriz ou desistir do game,
        # se não tiver nenhum erro de digitação,continua a execução no else.
        try:
            Escolha = int(input("Desistir - 0\nTrocar posição - 1 \n>>> "))
        except ValueError:
            print("Confira sua entrada")
            continue
        else:
            # 0 - Desistir do game
            if(Escolha == 0):
                print("Você desistiu!")
                break
            #1 - Mudar a posição (troca) de dois elementos da matriz.
            elif(Escolha == 1):
                while True:
                    try:
                        pos1 = int(input("Digite a posição 1 para troca - Formato ixj: "))
                    except ValueError:
                        print("Ops! confira sua entrada!")
                        continue
                    else:
                        break
                while True:
                    try:
                        pos2 = int(input("Digite a posição 2 para troca - Formato ixj: "))
                    except ValueError:
                        print("Ops! confira sua entrada!")
                        continue
                    else:
                        # Verificar se a jogada e valida usando a função VerificarJogada.Ela ira retornar um bool.
                        if(VerificaJogada(pos1,pos2,Jogo)):
                            break
                        else:
                            print("Confira sua entrada! ")
                            break
                Jogo = TrocarPosição(Jogo,pos1,pos2)
            #Tratativa de erro,caso o usuário digitar algo diferente de 0 ou 1.
            else:
                print("Ops! confira sua entrada!")
                continue
        #Verifica se o jogo está ganho.
        if(VerificaSeVenceu(Jogo)):
            print("Parabéns,você venceu o jogo!")
            break
        else:
            continue

def ConstruirMatriz():
    '''
    Construir uma matriz 4x4
    '''
    Matriz = []
    Lista = ['X',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    random.shuffle(Lista2)
    while len(Lista2) > 0:
        Linha = []
        for i in range(4):
            Linha.append(Lista[0])
            Lista.pop(0)
        Matriz.append(Linha)
    return Matriz

def TrocarPosição(Jogo,pos1,pos2):
    '''
    Trocar a posição de dois elementos da matriz e retorna a a lista já com os elementos trocados
    '''
    PosI = Jogo[pos1//10 - 1][pos1%10 - 1]
    PosJ = Jogo[pos2 // 10 - 1][pos2 % 10 - 1]
    Jogo[pos1 // 10 - 1][pos1 % 10 - 1] = PosJ
    Jogo[pos2 // 10 - 1][pos2 % 10 - 1] = PosI
    return Jogo

def VerificaSeVenceu(Jogo):
    '''
    Se a lista que contém o jogo for igual a Lista1 ou Lista2,a função retorá True para a função principal main
    '''
    Lista1 = [[1, 2, 3, 4][5, 6, 7, 8][9, 10, 11, 12][13, 14, 15,"X"]]
    Lista2 = [["X", 2, 3, 4][5, 6, 7, 8][9, 10, 11, 12][13, 14, 15,1]]
    if (Jogo == Lista1 or Jogo == Lista2):
        return True

def VerificaJogada(pos1,pos2,Jogo):
    '''
    Verificar se a jogada é valida

    retorna uma bool
    True - Jogada valida
    Falsa - Jogada invalida
    '''
    if(0 < pos1 < 45 and  0 < pos2 < 45):
        if(Jogo[pos1 // 10 - 1][pos1 % 10 - 1] == "X" or Jogo[pos2 // 10 - 1][pos2 % 10 - 1] == "X" ):
            return True
        else:
            return False
    else:
        return False

def ImprimeJogo(Matriz):
    '''
    Imprime o Jogo na tela em forma de matriz
    '''
    print(27*"_")
    for x in Matriz:
        linha = " "
        for y in x:
            if(type(y) == type(0)):
                if(y >= 10):
                    linha += str(y) + "   "
                else:
                    linha += str(y) + "    "
            else:
                linha += str(y) + "    "

        print(linha.rjust(25))
    print(27 * "_")

main()



