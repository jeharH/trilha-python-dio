# Peça um número entre 1 e 10. Se o número for inválido, peça novamente.



while True:
    numero = int(input('Digite um número: '))
    if numero >= 10 or numero == 0:
        print('Número inválido. Tente novamente!')
    else:
        print('Número válido!')
        break