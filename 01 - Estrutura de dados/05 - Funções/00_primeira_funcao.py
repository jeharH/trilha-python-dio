def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome): # Precisa de um parametro para funcionar, pois o parametro é pedido na função
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): # 
    print(f"Seja bem vindo {nome}!")


# exibir_mensagem()
# exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3() # Se na chamada da função, não for passado nada, é adotado o valor dado na função
exibir_mensagem_3(nome="Chappie") # aqui é adotado o valor dado na chamada da função
