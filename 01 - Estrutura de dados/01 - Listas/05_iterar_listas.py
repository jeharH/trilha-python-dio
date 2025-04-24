carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): # a função enumerate é usada para mostrar o indice de um objeto dentro do laço
    print(f"{indice}: {carro}")
