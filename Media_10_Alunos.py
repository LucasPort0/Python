'''
1- Faça um Programa que peça as quatro notas de 10 alunos ,calcule e armazene num vetor a média de cada aluno,imprima o número de alunos com média maior ou igual a 7.0

By Lucas Porto
Treinamento Linguagem Python
12/10/2021
'''


Exercicio 1
Media_Notas = []
Alunos_Na_Media = 0

while True:
    try:
        for NotaCount in range(10):
            notas = 0
            for AlunoCount in range(4):
                notas += int(input("Digite a nota %i do aluno numero %i: "%(AlunoCount + 1,NotaCount + 1)))
            Media_Notas.append(notas/4)
            print(notas/4)
        for Nota in Media_Notas:
            if(Nota >= 7.0):
                Alunos_Na_Media += 1
        print("O Numero de alunos na média é %i alunos"% Alunos_Na_Media)
    except ValueError:
        print("Somente Numeros Inteiros!")
