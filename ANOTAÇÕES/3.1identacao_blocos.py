def sacar (valor: float):
    saldo = 500
    if saldo >= valor:
        print('Valor sacado!')
        print('Retire o seu dinheiro na boca do caixa!')

    print('Obrigado por ser nosso cliente, tenha um bom dia!')


def depositar(valor: float):
    saldo_um = 500
    saldo_dois = valor
    saldo = saldo_um + valor
    print(f'Você tinha R$ {saldo_um}, o valor de {saldo_dois} foi depositado, totalizando R$ {saldo}')


sacar(100)
depositar(50)