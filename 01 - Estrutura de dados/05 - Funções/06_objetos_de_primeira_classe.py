def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def teste(a, b):
    return a + 5 + b + 10

def nomes(a, b):
    a = len(a)
    b = len(b)
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) # coloca a função dentro da variável
    print(f"O resultado da operação é = {resultado}") # chama a variável como resultado


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair)
exibir_resultado(5, 5, teste)
exibir_resultado('Jehar', 'Henrique', nomes)

vari = nomes
print(vari('Jehar', 'Henrique'))