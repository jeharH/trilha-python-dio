# Mostre todos os números pares de 1 a 50 usando for e range.

for par in range(0, 49):
    if par % 2 != 0:
        continue
    print(par, end=' ')