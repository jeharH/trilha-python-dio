# Peça dois números ao usuário e exiba a soma deles.
numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite outro número: '))


def somar(numero_um, numero_dois):
    soma = numero_um + numero_dois
    print(f'A soma dos dois números é: {soma}')

somar(numero_um, numero_dois)