nome = 'Jehar'


print(nome.upper()) # deixa tudo em maiusculo
print(nome.lower()) # deixa tudo em minusculo
print(nome.title()) # deixa a primeira letra maiuscula

texto = '    Olá Mundo '


print(texto)
print(texto.strip()) # tira o espaço da direita e esquerda
print(texto.lstrip()) # tira o espaço da direita
print(texto.rstrip()) # tira o espaço da esquerda

menu = 'Python'

print('####' + menu + '####')
print(menu.center(14, '#')) # faz a mesma coisa que a linha de cima, utilizando um método com 2 parametros

print('P-y-t-h-o-n')
print('-'.join(menu)) # itera letra por letra e coloca o parametro

for letra in menu:
    print(letra, end='-')