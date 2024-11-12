'''Faça um programa que mostre a tabuada dos números de 1 a 10.'''

def tabuadas():
    for numero in range(1, 11):  
        for i in range(1, 11):
            resultado = i * numero
            print (f"{numero} X {i} = {resultado}")
    

tabuadas()
