'''
FAÇA UM PROGRAMA PARA UMA LOJA DE TINTAS

O PROGRAMA DEVERÁ PEDIR O TAMANHO EM METROS QUADRADOS DA AREA A SER PINTADA.
CONSIDERE QUE A COBERTURA DA TINTA É DE 1 LITRO PARA CADA 3 METROS QUADRADOS E QUE A TINTA É VENDIDA EM LATAS DE 18 LITROS,
QUE CUSTAM 80,00.

INFORME AO USUÁRIO A QUANTIDADES DE LATAS DE TINTA A SEREM COMPRADAS E O PREÇO TOTAL.

By Lucas Porto
Treinamento Linguagem Python
20/07/2023
'''

metragem = int(input("AREA A SER PINTADA EM METROS QUADRADOS: "))

litros = metragem // 3

if metragem % 3 > 0:
    litros = litros + 1

latas = litros // 18

if litros % 18 > 0:
    latas = latas + 1

print (f"PARA PINTAR {metragem} METROS QUADRADOS, VOCÊ PRECISA DE {latas} LATAS E VAI TE CUSTAR R$ {latas * 80} ")



