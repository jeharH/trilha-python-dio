# Crie uma tupla com 5 cores favoritas suas.
# Mostre:
# - A primeira e a última cor
# - Se a cor "vermelho" está presente


cores = ('verde escuro', 'preto', 'verde musgo','rosa', 'verde água', )

print(cores[0])


for cor_vermelho in cores:
    if cor_vermelho == 'vermelho':
        print('A cor vermelha está presente')
        break
else: # Em Python, um for pode ter else, que só roda se o loop terminar sem um break.
        print('A cor vermelha não está presente!')

# if 'vermelho' in cores:
#     print('A cor vermelha está presente!')
# else:
#     print('A cor não está presente!')