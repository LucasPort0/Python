'''
Escreva um algoritmo que obtenha do usuário uma frase de tamanho entre 10 e 30 caracteres (faça a validação desse dado).

Após a frase ter sido digitada corretamente, faça a impressão dela na tela da maneira exata como foi digitada e, em seguida,
 remova os espaços da frase e imprima novamente, sem espaços.

By Lucas Porto
Treinamento Linguagem Python
01/08/2021
'''
while True:
        Frase = input("Digite uma frase de 10 a 30 caracteres: ")
        if(10 < len(Frase) < 30):
            print(Frase)
            print(Frase.replace(" ",""))
            #Utilizado quando não se quer usar o str.replace(" ","")
            #SemEspaco = ""
            #for palavra in Frase.split():
            #   SemEspaco += palavra
            #print(SemEspaco)
        else:
            print("OPS! confira a quantidade de caracteres!")



