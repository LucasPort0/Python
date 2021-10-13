'''
2- Escreva um programa que crie uma lista de elementos,até se entrar -1 e depois imprima todos os numeros da lista que são maiores que 10.

By Lucas Porto
Treinamento Linguagem Python
12/10/2021
'''
Lista_Elementos = []
Possui_maior_que_10 = True
try:
    while True:
        numero = int(input("Digite um numero: "))
        if(numero != -1):
            Lista_Elementos.append(numero)
            Possui_maior_que_10 = False
        else:
            break
    for item in Lista_Elementos:
        if(item > 10):
            print("%i é maior que 10"% item)
except ValueError:
    print("Sua entrada está invalida!")
else:
    if (Possui_maior_que_10):
        print("Você não digitou nenhum número maior do que 10!")
