numeros = [1, 4, 7, 9, 34, 66, 77, 99, 10, 44]
pares = []

for par in numeros:
    if par % 2 == 0:
        pares.append(par)

print(pares)