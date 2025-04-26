contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)


# remove a chave e retorna o valor
# se não encontrar a chave, ele da um erro, porém se tiver um segundo argumento, ele não da erro, apenas retorna o segundo argumento