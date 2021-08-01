'''
Escreva um algoritmo que imprima na tela as horas no formato H:M:S dentro de um intervalo definido pelo usuário.
O usuário deverá delimitar o intervalo de horas que deseja imprimir (por exemplo, das 7h até as 14h).

Valide os dados de entrada para que seu programa só aceite valores válidos para hora (de 0 até 23h)
e que a hora inicial digitada não seja maior que a final.
Caso isso aconteça, o usuário deverá digitar o intervalo novamente.

By Lucas Porto
Treinamento Linguagem Python
01/08/2021
'''

while True:
    try:
        #Recebe os valores do intervalo
        HoraInicial = int(input("Hora inicial: "))
        HoraFinal = int(input("Hora Final"))
        #Checa se o valor está entre 0 e 23
        if(0 <= HoraInicial <= 23 and 0 <= HoraFinal <= 23):
            #Hora inicial é menor que a hora final
            if(HoraInicial < HoraFinal):
                # Sequencias de for para imprimir a hora
                for hora in range(HoraInicial, HoraFinal + 1):
                    for minutos in range(60):
                        for segundos in range(60):
                            print(f"{hora}:{minutos}:{segundos}")
            else:
                print("Certifique que a hora final é maior que a hora incial!")
        else:
            print("OPS! somente valores entre 0 e 23")
    except ValueError:
        print("OPS! somente numeros INTEIROS!!!")







