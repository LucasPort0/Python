
'''
Faça um programa que leia 20 números inteiros e armazene-os num vetor.Armazene os números pares no vetor PAR e
os números IMPARES no vetor impar.Imprima os três vetores.

By Lucas Porto
Treinamento Linguagem Python
26/09/2021
'''
import random

numeros_pares = []
numero_impares = []
numeros = []

for i in range(20):
    num = random.randint(0,1000)
    if(num % 2 == 0):
        numeros_pares.append(num)
    else:
        numero_impares.append(num)
    numeros.append(num)

print("Temos %i números pares e %i numeros impares"%(len(numeros_pares),len(numero_impares)))
print("Conjunto Par: ",numeros_pares)
print("Conjunto impar: ",numero_impares)
print("Numeros sorteados: ",numeros)
