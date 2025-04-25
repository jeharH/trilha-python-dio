contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", 'extra' : {'idade' : '21'}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

nome = contatos['guilherme@gmail.com']['nome']
print(nome)

idade = contatos['melaine@gmail.com']['extra'] ['idade']
print(idade)

# é possível colocar dicionarios dentro de outros dicionários os aninhando como no exemplo acima
# para acessar dicionários é necessários chamar a variável onde está armazenado o dicionário e entre conchetes colocar a chave desejada para acessar determinado valor
# para acessar um valor de um dicionário aninhado, é necessário informar entre conchetes as duas chaves ou mais chaves onde o valor está armazenado