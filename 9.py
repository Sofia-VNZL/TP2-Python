'''Faça um programa que leia uma sequência de números, terminada pelo número zero, e mostre-os na ordem invertida.

Implemente uma função para ler a lista de números e outra para exibir a lista invertida.
Utilize apenas os comandos ensinados em aula.'''

def entrada_numeros():
    
    lista = []

    while True:
        numero = int(input("Digite um número inteiro positivo (ou 0 para terminar): "))

        if numero == 0:
            print("fim do Programa")
            break

        elif numero < 0:
            print("Por favor, digite um número positivo.")

        else:
            lista.append(numero)
    print(f" A lista de números digitados foi: {lista}")
    print(f"A mesma lista invertida é: {lista[::-1]}")

entrada_numeros()