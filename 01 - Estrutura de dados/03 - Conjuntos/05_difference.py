conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b) # retorna o que não está no conjunto B, no caso 1
print(resultado)

resultado = conjunto_b.difference(conjunto_a) # retorna o que não está no conjunto A, no caso 4
print(resultado)
