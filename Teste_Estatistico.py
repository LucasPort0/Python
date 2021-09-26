"""
Escreva um programa para simular o jogo das portas. Faça um programa que tenha
a saída como a seguinte:

Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!
Escolha uma porta: 3
Você escolheu a porta 3, mas
eu lhe informo que na porta 2 há um bode.
Deseja trocar de porta (1 - Sim/ 0 - Não): 1
Ganhou um carro!

By Lucas Porto
Treinamento Linguagem Python
25/09/2021
"""
import random
while True:
    try:
        porta_escolhida = int(input("Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!\nEscolha uma porta das 3 portas: "))
        porta_sorteada = random.randint(1, 3)
        porta_sugerida = random.randint(1, 3)
        while(porta_escolhida == porta_sugerida):
            porta_sugerida = random.randint(1, 3)
        escolha = int(input("Você escolheu a porta %d, mas eu lhe informo que na porta %d há um bode.\n Deseja trocar de porta (1 - Sim/ 0 - Não):"%(porta_escolhida,porta_sugerida)))
        if(escolha == 1):
            porta_escolhida = int(input("Escolha uma porta das 3 portas: "))
        elif(escolha == 0):
            print("Voce manteve a porta %d"%porta_escolhida)
        if(porta_sorteada == porta_escolhida):
            print("Voce ganhou um carro!")
        else:
            print("Infelizmente não foi desta vez,o carro estava na porta %d"%porta_sorteada)

    except ValueError:
        print("OPS! Sua entrada está errada!")
    finally:
        print("_" * 60)