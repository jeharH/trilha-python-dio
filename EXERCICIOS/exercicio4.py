# Peça um número e mostre a tabuada dele de 1 a 10.

numero = int(input('Digite um número: '))

def tabuada(numero):
    for i in range(1, 11):
        resultado = i * numero
        print(f'{numero} x {i} = {resultado}')

tabuada(numero)