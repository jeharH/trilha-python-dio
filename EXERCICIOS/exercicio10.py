# Peça números ao usuário até ele digitar 0. Mostre a soma total no final.

soma = 0

while True:
    numero = int(input('Digite um número: '))
    if numero != 0:
        soma += numero
    else:
        print(f'A soma dos números digitados é: {soma}')
        break