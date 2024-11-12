''' Estatísticas de uma Lista

Faça um programa que mostre o menor, o maior, a soma e a média dos elementos da lista:
[10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

Utilize apenas os comandos ensinados em aula.'''

def maior_menor_media():
    lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    print(f"""na lista {lista}:
        o maior numero é: {maior}
        o menor numero é: {menor}
        e a média é: {media}""")

maior_menor_media()