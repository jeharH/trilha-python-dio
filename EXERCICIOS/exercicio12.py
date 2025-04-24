# Peça um número ao usuário e calcule o fatorial dele (ex: 5! = 5*4*3*2*1)

numero = int(input('Digite um número: '))
resultado = 1

for i in range(numero, 0, -1):
    resultado = resultado * i
    
print(resultado)