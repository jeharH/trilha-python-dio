# Peça uma senha até que o usuário digite "1234".

senha = 1234

senha_usuario = int(input('Digite sua senha: ')) # Tirar essa sinha caso use o 2 método de fazer

while senha_usuario != senha:
    print('Senha incorreta! Tente novamente!')
    senha_usuario = int(input('Digite sua senha: '))

print('Senha correta! Acesse sua conta!')


# OUTRO MÉTODO DE FAZER

while True:
    senha_usuario = int(input('Digite sua senha: '))
    if senha_usuario == senha:
        ('Senha correta! Acesse sua conta!')
        break
    else:
        print('Senha incorreta! Tente novamente!')