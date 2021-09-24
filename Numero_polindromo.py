
'''
By Lucas Porto
Treinamento Linguagem Python
23/09/2021


Dizemos que um número natural n é palíndromo (3) se
    o 1º algarismo de n é igual ao seu último algarismo,
    o 2º algarismo de n é igual ao penúltimo algarismo,
    e assim sucessivamente.

Exemplos:
567765 e 32423 são palíndromos.
567675 não é palíndromo.
Dado um número natural   n > 10 , verificar se n é palíndrome.

567765
iguais
567765
'''
while True:
    numero = input("Digite um numero maior que 10: ")
    if(numero.isdigit()):
        if(int(numero) > 10):
            numero_invertido = numero[::-1]
            if(numero == numero_invertido):
                print("Esse numero é polindromo")
            else:
                print("Esse numero não é polindromo")
        else:
            print("Somente numeros maiores que 10")
    else:
        print("Somente numeros!")
        


