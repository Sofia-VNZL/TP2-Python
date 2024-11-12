'''Soma de Duas Listas

Faça um programa que some as seguintes listas:
[1, 2, 3, 4, 5, 6, 7, 8]
[10, 20, 30, 40, 50, 60, 70, 80]

Mostre o resultado da soma em uma terceira lista.
Exemplo:
A soma das listas seria:
[11, 22, 33, 44, 55, 66, 77, 88]

Utilize apenas os comandos ensinados em aula.'''

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]

def soma():
    lista3 = [a + b for a, b in zip(lista1, lista2)]
    
    print(f"A soma das listas é: {lista3}")

soma()