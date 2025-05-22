# esse código cria uma função que pega os arquivos da pasta e joga eles dentro  de arquivos_extraidos

meses_sistema = ["jan2022","fev2022","mar2022","abr2022","mai2022","jun2022","jul2022","ago2022","set2022","out2022","nov2022","dez2022","jan2021","fev2021","mar2021","abr2021","mai2021","jun2021","jul2021","ago2021","set2021","out2021","nov2021","dez2021","jan2020","fev2020","mar2020","abr2020","mai2020","jun2020","jul2020","ago2020","set2020","out2020","nov2020","dez2020","jan2019","fev2019","mar2019","abr2019","mai2019","jun2019","jul2019","ago2019","set2019","out2019","nov2019","dez2019","jan2018","fev2018","mar2018","abr2018","mai2018","jun2018","jul2018","ago2018","set2018","out2018","nov2018","dez2018","jan2017","fev2017","mar2017","abr2017","mai2017","jun2017","jul2017","ago2017","set2017","out2017","nov2017","dez2017"]
print(len(meses_sistema))



import os # biblioteca que permitte perocrrer pastas dentro do computador

arquivos_extraidos = []

def pegar_arquivos_pasta(pasta): # rece um pasta com informação
    lista_arquivos = os.listdir(pasta) # a biblioteca os tem a função listdir que lista todos os arquivos de dentro de um diretório
    # se tiver txt e vendas no nome do arquivo, então eu vou pegar o nome do mês
    for arquivo in lista_arquivos:
        if '.txt' in arquivo and 'Vendas' in arquivo:
            # significa que eu quero pegar o nome do mês
            nome_mes = arquivo.split()[-1].replace('.txt', '') # o split separa o nome do arquivo por elementos, indice [-1] pega o ultimo elemento da lista e replace troca alguma parte do nome do arquivo
            arquivos_extraidos.append(nome_mes) # adiciona o nome do arquivo dentro da variavel
        elif '.txt' not in arquivo: # se é uma pasta
            pegar_arquivos_pasta(f'{pasta}/{arquivo}') # se a varialvel arquivo for 'Outros anos', ele pega o próprio arquivo dentro da pasta 'Arquivos'

    # caso o contrário, não vou ffazer nada
    pass # pega os arquivos dessa pasta

pegar_arquivos_pasta('Arquivos') # chama a função e coloca a pasta 'Arquivos' como parâmetro
print(arquivos_extraidos)

for mes in meses_sistema:
    if mes not in arquivos_extraidos:
        print(mes)