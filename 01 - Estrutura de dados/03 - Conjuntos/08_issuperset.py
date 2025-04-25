conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado) # todos os elementos de B, estão em A?

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado) # todos os elementos de A, estão em B?