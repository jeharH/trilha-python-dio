# Peça 5 números ao usuário e guarde numa lista.
# Depois, exiba:
# - A lista original
# - A lista em ordem crescente
# - A lista em ordem decrescente

lista = []

for i in range(0,5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)