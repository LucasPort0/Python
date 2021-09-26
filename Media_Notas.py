'''
Faça um programa que leia um certo número de  notas,mostre as notas e a média na tela

By Lucas Porto
Treinamento Linguagem Python
26/09/2021
'''
notas = []
soma_notas = 0

total_notas = int(input("Quer fazer a soma de quatas notas?: "))
for i in range(0,total_notas):
    notas.append(int(input("Digite a nota de numero %i: "%(i + 1))))
    soma_notas += notas[i]

for indice,nota in enumerate(notas):
    print("Nota numero %i é %i"%(indice + 1,nota))

media = soma_notas/total_notas
print("A média das notas é %.2f"%media)
