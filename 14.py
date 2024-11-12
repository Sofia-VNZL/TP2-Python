'''Entrada Validada de Números

Faça um programa que leia um número do teclado e garanta que ele seja maior ou igual a zero.

Enquanto a entrada não for válida, o programa deve exibir uma mensagem de erro e pedir uma nova entrada.
Utilize apenas os comandos ensinados em aula.'''

def validacao():
    while True:
        num = int(input("Digite um número maior ou igual a zero (0): "))

        if num == 0:
            print(f"Certo! {num} é igual a zero (0)")
            break
        elif num > 0:
            print(f"Certo! {num} é maior que zero (0)")
            break
        else:
            print(f"{num} não é maio ou igual a zero (0), tente novamente: ")

validacao()

