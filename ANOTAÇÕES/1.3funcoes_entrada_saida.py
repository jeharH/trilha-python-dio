#EXEMPLO

nome = 'Guilherme'
sobrenome = 'Carvalho'

print(nome, sobrenome)
print(nome, sobrenome, end='...\n') # adiciona '...' no final e também uma quebra de linha com '\n'
print(nome, sobrenome, sep='#') # adiciona um separador, que nesse caso é o '#', mas nornalmente é um ' '

nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')

print(nome, idade) # por padrão ele já adiciona a quebra de linha, porem se eu indicar um separador, essa quebra de linha some
print(nome, idade, end='...\n')
print(nome, idade, sep='#', end='..\n')
print(nome, idade, sep='#')