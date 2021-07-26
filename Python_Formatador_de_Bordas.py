
'''
By Lucas Porto
Treinamento Linguagem Python
26/07/2021
'''
def borda(palavra):
    tamanho = len(palavra) -2
    print("+", "-" * tamanho,"+")
    print(f"|{palavra}|")
    print("+", "-" * tamanho, "+")



borda(input("Digite a palavra: "))