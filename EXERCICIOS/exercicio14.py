# Mostre um menu com 3 opções (ex: 1 - Somar, 2 - Subtrair, 3 - Sair)
# Execute a operação escolhida e volte ao menu até o usuário sair.

while True:
    escolha = int(input(f'''
################ MENU ################
Escolha uma opção: [1] SOMAR
                   [2] SUBTRAIR
                   [3] SAIR
######################################
'''))
    if escolha == 1:
        print('Opção escolhida: SOMA')
        numero_um = int(input('Digite um número: '))
        numero_dois = int(input('Digite outro número: '))
        soma = numero_um + numero_dois
        print(f'A soma de {numero_um} + {numero_dois} é {soma}.')
    elif escolha == 2:
        print('Opção escolhida: SUBTRAÇÃO')
        numero_um = int(input('Digite um número: '))
        numero_dois = int(input('Digite outro número: '))
        subtracao = numero_um - numero_dois
        print(f'A subtração entre {numero_um} e {numero_dois} é {subtracao}.')
    else:
        break