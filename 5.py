'''Uma progressão aritmética (PA) é uma sequência numérica onde cada termo, a partir do segundo, é igual à soma do termo anterior com uma constante.

A constante é a diferença entre o segundo e o primeiro número.
Faça um programa que receba dois números inteiros e, a partir dessa informação, gere uma sequência em PA.'''


primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
num = int(input("Digite o numero de termos da PA: "))

def criar_pa(primeiro, razao, num):
    
    pa = []
    for i in range(num):
        termo = primeiro + i * razao
        pa.append(termo)
    return pa
    
sequencia = criar_pa(primeiro, razao, num)

print(f"A Progressão Aritmética é: {sequencia}")
