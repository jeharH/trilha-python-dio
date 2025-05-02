def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args) # o .join concatena todas as strings de args, e o '\n' separa cada por linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # nessa linha, o kwargs.items() pega os valores 'chave:valor' e itera os mesmo, com o for, jogando as chaves na variavel CHAVE e os valores na variável VALOR. Depois é exibido a chave com .title deixando os valores da chave com a primeira letra maiuscula e em seguida é exibido o valor da chave. Todos esses valores são concatenados com o .join e colocados um em cada linha com o '\n'
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # cria a variável mensagem e coloca dentro dela a exibição da data_extenso, pula duas linhas, texto, pula duas linhas, meta_dados
    print(mensagem) # exibe a varável mensagem


exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
) # chama a função, passando os dados requisitados na função (data_extenso, *args, **kwargs)


# a primeira linha e coloca no parametro: data_extenso
# os proximos valores separarados por virgula, entram todos dentro de *args
# os valores 'chave : valor' entram dentro de **kwargs