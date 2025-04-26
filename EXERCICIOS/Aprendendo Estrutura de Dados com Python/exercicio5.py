# Peça notas de alunos (quantas quiser) e guarde em uma lista.
# Depois, mostre:
# - Média das notas
# - Maior e menor nota


notas = []

def media(notas):
    contador = 0
    for soma in notas:
        contador = contador + soma
    quantidade = len(notas)
    media = contador / quantidade
    return media # retorna o valor da MÉDIA



while True:
    nota_aluno = input('''
#### BEM VINDO A CALCULADORA DE MÉDIA ####

Adicione uma nota e quando finalizar digite SAIR:
''') # repete o while até atingir alguma condição

    if nota_aluno.upper() == 'SAIR': # com o .upper(), o usuário pode digitar SAIR, Sair ou sair
        if notas: # Só calcula a média se tiver pelo menos uma nota na lista, é como se fosse um if notas == True

            resultados = media(notas) # coloca a média dentro de uma variável e mostra no print
            print(f'A média das notas é: {resultados} ')
        else:
            print('Nenhuma nota foi adicionada!') 
        break
    else:
        try: # uma forma de testar algo que possa dar erro, sem dar erro, no caso se for digitado 'oi', iria dar erro, porém com o try, o python não trava e o except é executado
            nota = float(nota_aluno) # converte a nota para float (antes era string)
            notas.append(nota) # adiciona a nota na lista
        except ValueError: # executa caso o try de erro
            print('Você não digitou um valor válido')

# ouuuuuu

notas = []

while True:
    entrada = input("Digite uma nota ou 'SAIR' para finalizar: ")

    if entrada.upper() == 'SAIR':
        if len(notas) > 0:
            soma = sum(notas)
            media = soma / len(notas)
            print(f"A média das notas é: {media}")
        else:
            print("Nenhuma nota foi inserida.")
        break
    else:
        nota = float(entrada)
        notas.append(nota)
