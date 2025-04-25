conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado) # todos os elementos do conjunto B, não estão presentes no conjunto A

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado) # todos os elementos do conjunto C, não estão presenetes no conjunto A