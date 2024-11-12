'''Números Maiores ou Iguais à Média

Faça um programa que leia uma sequência de números, terminada pelo número zero, e armazene-os em uma lista.

O programa deve mostrar apenas os números maiores ou iguais à média dos elementos lidos.
Implemente uma função para ler a lista e outra para exibir os números filtrados.
Utilize apenas os comandos ensinados em aula.'''

def entrada_numeros():
    
    lista = []

    while True:
        numero = int(input("Digite um número inteiro positivo (ou 0 para terminar): "))

        if numero == 0:
            break

        elif numero < 0:
            print("Por favor, digite um número positivo.")

        else:
            lista.append(numero)
    return lista

def operacao(lista):

    if not lista:
        print("Não há valores na lista")
        return
    
    print(f"Lista digitada: {lista}")

    media = sum(lista) / len(lista)
    print(f"Média dos elementos: {media:.2f}")

    igual_maior = [num for num in lista if num >= media]
    print(f"Números maiores ou iguais a {media}: {igual_maior}")

operacao(entrada_numeros())