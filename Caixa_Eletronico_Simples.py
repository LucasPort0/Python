'''
FAÇA UM PROGRAMA PARA UM CAIXA ELETRONICO. O PROGRAMA DEVERA PERGUNTAR AO USUARIO O VALOR DO SAQUE E DEPOIS INFORMAR
QUANTAS NOTAS DE CADA VALOR SERÃO FORNECIDAS. AS NOTAS DISPONIVEIS SERÃO AS DE 1,5,10,50,100 REAIS. O VALOR MINIMO É
DE 10 REAIS E O MAXIMO DE 600 REAIS. O PROGRAMA NÃO DEVE SE PREOCUPAR COM A QUANTIDADE DE NOTAS EXISTENTES NA MAQUINA

	EXEMPLO 1 - PARA SACAR A QUANTIA DE 256 REAIS, O PROGRAMA FORNECE DUAS NOTAS DE 100, UMA NOTA DE 50, UMA NOTA DE 5 E UMA NOTA DE 1
	EXEMPLO 2 - PARA SACAR A QUA TIA DE 399 REAIS, O PROGRAMA FORNECE TRES NOTAS DE 100, UMA NOTA DE 50, QUANTRO NOTAS DE 10M UMA NOTA DE 5 E QUATRO NOTAS DE 1

By Lucas Porto
Treinamento Linguagem Python
26/07/2023
'''

while True:
    try:
        Nota_100 = 0
        Nota_50 = 0
        Nota_10 = 0
        Nota_5 = 0
        Nota_2 = 0
        Nota_1 = 0
        Valor_Saque = int(input("Digite o valor a ser sacado: "))
        if (10 <= Valor_Saque <= 600):
            if (100 <= Valor_Saque <= 600):
                Nota_100 = Valor_Saque // 100
                Valor_Saque -= Nota_100 * 100
            if (50 <= Valor_Saque < 100):
                Nota_50 = Valor_Saque // 50
                Valor_Saque -= Nota_50 * 50
            if (10 <= Valor_Saque < 50):
                Nota_10 = Valor_Saque // 10
                Valor_Saque -= Nota_10 * 10
            if (5 <= Valor_Saque < 10):
                Nota_5 = Valor_Saque // 5
                Valor_Saque -= Nota_5 * 5
            if (2 <= Valor_Saque <= 5):
                Nota_2 = Valor_Saque // 2
                Valor_Saque -= Nota_2 * 2
            if (1 <= Valor_Saque):
                Nota_1 = Valor_Saque
            print(f"Notas 100 reais: {Nota_100} \n Notas 50 reais: {Nota_50} \n Notas 10 reais: {Nota_10} \n Notas 5 reais: {Nota_5} \n Notas 2 reais: {Nota_2} \n Notas 1 real: {Nota_1}")
        else:
            print("Saque minimo é de 10 reais e maximo de 600 reais")
    except ValueError:
        print("Confira o valor Digitado!")


