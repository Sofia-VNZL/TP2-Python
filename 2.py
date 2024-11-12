'''Faça um programa que calcule a soma e a média dos números de 1 a 100'''

#tentei evitar as variaveis globais dessa vez e deixar tudo em partes em funções separadas.

def entradas():
    primeiro = int(input("Qual o primeiro numero do intervalo?: "))
    ultimo = int(input("Qual o último numero do intervalo?: "))
    intervalo = range(primeiro, ultimo + 1)
    return intervalo
    

def soma(intervalo):
    soma = sum(intervalo)
    return soma

def media(intervalo):
    soma_intervalo = soma(intervalo)
    media = soma_intervalo / len(intervalo)
    return media

def soma_media():
    print("Deseja saber a soma e a média dos números de um intervalo?")
    print(f"por exemplo, a soma do 1 ao 100 é {soma(range(1, 101))} e a média é {media(range(1, 101))}")
    
    intervalo = entradas()  

    soma_intervalo = soma(intervalo)
    media_intervalo = media(intervalo)
    
    print(f"A soma dos numeros entre {intervalo[0]} e {intervalo[-1]} é {soma_intervalo}.")
    print(f"E a média dos números entre {intervalo[0]} e {intervalo[-1]} é {media_intervalo:.2f}.")


soma_media()
