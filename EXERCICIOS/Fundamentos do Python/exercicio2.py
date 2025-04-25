# Peça um número ao usuário e diga se ele é par ou ímpar.

def verificar_par_impar():
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print('O número é par!')
    else:
        print('O número é impar!')

verificar_par_impar()