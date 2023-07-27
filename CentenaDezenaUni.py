'''
    Faça um programa que leia um numero inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
    unidades do mesmo. Observando os termos no plural e colocação do "e", da virgula entre outros, Exemplo:
        326 - 3 centenas, 2 dezenas e 6 unidades
        12 - 1 dezenas e 2 unidades
    Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.

By Lucas Porto
Treinamento Linguagem Python
27/07/2023
'''
try:
    dezena, centena, unidade = 0, 0, 0
    dez, cent, uni = "Dezena", "Centena", "Unidade"

    numero = int(input("Digite um numero inteiro menor que 1000: "))
    if (0 <= numero < 1000):
        centena = numero // 100
        dezena = numero % 100 // 10
        unidade = numero - (centena * 100 + dezena * 10)

        if (centena > 0):
            if(centena > 1):
                cent = "Centenas"
            print(centena, cent)
        if (dezena > 0):
            if (dezena > 1):
                dez = "Dezenas"
            print(dezena, dez)
        if(unidade > 0):
            print(unidade, uni)
    else:
        print("Somente um numero inteiro menor que 1000.")
except ValueError:
    print("Confira os valores digitados.")
