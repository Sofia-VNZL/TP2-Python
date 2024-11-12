'''Separação de Pares e Ímpares

Faça um programa que, a partir da lista:
[10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
crie duas listas: uma com números pares e outra com números ímpares.

Implemente uma função para determinar se um número é par ou ímpar.
Utilize apenas os comandos ensinados em aula.'''

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

def par(num):
   
    return num % 2 == 0

def separar():
    pares = []
    impares = []

    for num in lista:
        if par(num):
            pares.append(num)
        else:
            impares.append(num)

    print(f"Lista de números pares:", pares)
    print(f"Lista de números ímpares:", impares)

separar()



