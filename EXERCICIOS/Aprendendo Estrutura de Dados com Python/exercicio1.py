# Crie uma lista vazia e peça ao usuário para adicionar itens de compra.
# Quando ele digitar "sair", mostre a lista final com todos os itens.

lista = []


# while True:
#     funcao = int(input('''
# Escolha a opção:
# [1] ADICIONAR ITEM
# [2] SAIR
# '''))
#     if funcao == 1:
#         item = input('Qual item você quer adicionar? Digite: ')
#         lista.append(item)
#     else:
#         print(lista)
#         break

while True:
    item = input('Adicione um item: ')
    if item == 'sair':
        print(lista)
        break
    else:
        lista.append(item)