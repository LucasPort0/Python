'''
By Lucas Porto
Treinamento Linguagem Python
25/09/2021

 Faca um programa que peça o raio de um circulo,calcule e mostre sua área
'''
import math as m
while True:
    try:
        raio_circuferencia = int(input("Digite o raio da circuferencia: "))
        area_circunferencia = m.pi * m.pow(raio_circuferencia,2)
        print("Uma circuferencia de raio %d tem area aproximadamente igual a %.2f" %(raio_circuferencia,area_circunferencia))
    except ValueError:
        print("Somente numeros inteiros!")

    finally:
        print("-" * 30)
