'''Faça um programa que leia uma sequência de caracteres terminada por um ponto (.) e mostre o número de vogais digitadas.

Cada caractere deve ser digitado/lido separadamente.'''

def contagem_vogais():
    respostas = []
    vogais = "AEIOU"
    fim = "."

    while True:
        entrada = input("Entre com um caractere: ").upper()

        
        if len(entrada) != 1:
            print("Por favor, digite apenas um caractere por vez.")
            continue  
        
        
        if entrada == fim:
            break

        
        respostas.append(entrada)
    
    
    num_vogais = sum(1 for char in respostas if char in vogais)
    print(f"Número de vogais digitadas: {num_vogais}")


contagem_vogais()

