def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}

    for i in string:
        if i in contador:
            contador[i] = contador[i] + 1
        else:
            contador[i] = 1
    return contador
       
#TODO: Itere através de cada caractere na string string.
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
    
    

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)