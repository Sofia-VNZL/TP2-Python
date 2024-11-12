''' Busca de Elemento na Lista

Faça um programa que leia um número do teclado e verifique se ele está presente na lista:
[20, 10, 30, 40, 60, 50, 70, 90, 80, 100].

Se o número for encontrado, o programa deve retornar sua posição na lista.
Caso contrário, deve retornar -1, indicando que o número não foi encontrado.
Implemente uma função para buscar o elemento na lista.
Utilize apenas os comandos ensinados em aula.'''

lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]
num = int(input("Digite um número inteiro para saber se está na lista: "))

def procurar_index(lista, num):

    if (num in lista):
        posicao = lista.index(num)
        return posicao
    else:
        return -1

def exibir():
    resultado = procurar_index(lista, num)

    if (resultado != -1):
        print(f"A posição de {num} digitado na tabela é {resultado}")
    else:
        print(f"O resultado é {resultado}, {num} não está na lista")

exibir()