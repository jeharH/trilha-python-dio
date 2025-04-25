# Mostre os números primos entre 1 e 100.

for numero_primo in range(2, 101):
    eh_primo = True
    for i in range(2, numero_primo): # itera cada número entre 2 e o numero iterado no laço anterior
        if numero_primo % i == 0: # verifica se o numero_primo (atual) tem algum divisivel que reste 0 entre os numeros iterado acima
            eh_primo = False
            break
    if eh_primo:
        print(numero_primo, end=' ')