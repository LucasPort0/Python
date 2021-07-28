
'''
By Lucas Porto
Treinamento Linguagem Python
28/07/2021
'''
#Escreva um algoritmo que encontre todos os números primos de um valor inicial até um valor final. Imprima na tela todos eles.

Quantidade_Primos = 0
Numeros_Primos = []
while True:
    try:
        Num_Inicial = int(input("Digite o numero inicial: "))
        Num_Final = int(input("Digite o numero final: "))
    except ValueError:
        print("Confira o valor digitado")
    else:
        for num in range(Num_Inicial,Num_Final):
            Quantidade_Divisores = 0
            for natural in range(1,Num_Final):
                if(num % natural == 0):
                    Quantidade_Divisores += 1
            if(Quantidade_Divisores == 2):
                Quantidade_Primos += 1
                Numeros_Primos.append(num)
        print(f"Entre {Num_Inicial} e {Num_Final} temos {Quantidade_Primos} números primos que são:\n {Numeros_Primos}")
    finally:
        print("_" * 100)



