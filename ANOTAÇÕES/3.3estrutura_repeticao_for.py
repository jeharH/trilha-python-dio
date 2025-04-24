texto = input('Digite um tetxto:')
VOGAIS = 'AEIOU'

for letra in texto: # percorre cada item dentro da variável 'texto' e joga um de cada vez dentro da variável letras
    if letra.upper() in VOGAIS:
        print(letra, end='')

else:
    print() # adiciona uma quebra de linha
    print('Executa no final do laço')

for numero in range (0, 51, 5): # exemplo utilizando  a função range
    print(numero, end=' ')