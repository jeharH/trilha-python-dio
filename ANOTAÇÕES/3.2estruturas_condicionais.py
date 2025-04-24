maior_idade = 18
idade_especial = 17

idade = int(input('Informe sua idade: '))

if idade >= 18:
    print('Maior de idade! Pode tirar a CNH.')

elif idade >= idade_especial:
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas.')

elif idade >= 16:
    print('Você não é maior de idade! Mas pode tirar CNH nos EUA.')

else:
    print('Você é menor de idade! Não pode tirar a CNH.')