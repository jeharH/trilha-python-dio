conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado) # todos os elementos de A pertencem também a B

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado) # todos os elementos de B pertencem também a A
