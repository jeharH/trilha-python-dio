# O programa escolhe um número entre 1 e 10 e o usuário tenta adivinhar.
# Repita até acertar.

import random

numero = int(input('Tente advinhar o número sorteado: ')) # Tirar essa sinha caso use o 2 método de fazer
numero_sorteado = random.randint(1, 11) # o método randint da biblioteca random sorteia um número aleatório e joga dentro da variável

while numero != numero_sorteado:
    print('Você errou! Tente novamente.')
    numero = int(input('Tente advinhar o número sorteado: '))

print('Você acertou!')


# OUTRA FORMA DE FAZER

while True:
    numero = int(input('Tente advinhar o número sorteado: '))
    if numero != numero_sorteado:
        print('Você errou! Tente novamente.')
    else:
        print('Você acertou!')
        break