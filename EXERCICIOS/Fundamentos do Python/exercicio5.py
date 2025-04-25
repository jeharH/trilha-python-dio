# Peça 5 números ao usuário e mostre a soma total.

soma = 0

for i in range(0, 5):
    numero = float(input('Digite um número: '))
    soma = soma + numero


print(f'A soma de todos os número é: {soma}')