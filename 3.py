'''Faça um programa que leia uma sequência de números inteiros positivos, terminada por zero. Para cada número lido, mostre seu fatorial.

Implemente uma função para o cálculo do fatorial.'''

def fatorial(n):
    if n == 1 or n == 0:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado
    
def entrada_numeros():
    
    while True:
        numero = int(input("Digite um número inteiro positivo (ou 0 para terminar): "))

        if numero == 0:
            print("fim do Programa")
            break

        elif numero < 0:
            print("Por favor, digite um número positivo.")

        else:
            print(f"O fatorial de {numero} é {fatorial(numero):.2f}")



entrada_numeros()
