nome = 'Guilherme'
idade = 28
profissao = 'Progamador'
linguagem = 'Python'
saldo = 45.458

dados = {'nome': 'Guilherme', 'idade': 28}


print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {} Idade: {}'.format(nome, idade))
print('Nome: {0} Idade: {1}'.format(nome, idade))
print('Nome: {name} Idade: {age}'.format(name=nome, age=idade))
print('Nome: {nome} Idade: {idade}'.format(**dados))
print(f'Nome: {nome} Idade: {idade}')

print(f'{saldo:.2f}')