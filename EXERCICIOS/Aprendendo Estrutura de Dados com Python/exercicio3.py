# Peça vários números ao usuário e armazene em uma lista.
# Depois, mostre a lista sem duplicatas (use um conjunto).


lista = []


while True:
    numeros = input('Digite um número ou digite [SAIR]: ')
    if numeros == 'SAIR':
        conjunto = set(lista)
        print(conjunto)
        break
    else:
        lista.append(numeros)