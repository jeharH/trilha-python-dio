conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com saldo do cheque_especial!')
    else:
        print('Não foi possível realizar o saque!')

elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Não foi possível realizar o saque! Verifique o saldo e tente novamente')

else:
    print('Sistema não reconheceu o tipo de conta, entre em contato com seu gerente.')