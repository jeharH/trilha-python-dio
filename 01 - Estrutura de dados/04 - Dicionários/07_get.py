contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado) # retorna None pois não encontrou o valor da chave, pois a mesma não existe

resultado = contatos.get("chave", {})  # {}
print(resultado) # se não encontrar a chave, devolve um valor defalt

resultado = contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado) # retorna a chave que existe


# verificar se a chave existe ou não no dicionário