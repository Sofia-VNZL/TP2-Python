'''Faça um programa que leia um intervalo inferior e superior e mostre os números primos encontrados nesse intervalo.

Por exemplo, para o intervalo de 5 a 10, a saída será: 5, 7.
O programa também deve mostrar a quantidade de números primos encontrados.
Implemente uma função para verificar se um número é primo.'''

import math

primero = int(input("Digite o primeiro número do intervalo: "))
ultimo = int(input("Digite o ultimo número do intervalo: "))

def primo(num):
    if num < 2:
        return False
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True


def leitura():

    primos = []

    for i in range(primero, ultimo + 1):
        if primo(i):
            primos.append(i)

    print(f"Os primos nessa equencia são: {primos}")

leitura()
