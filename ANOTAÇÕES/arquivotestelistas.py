import requests

url = "https://official-joke-api.appspot.com/random_joke"
resposta = requests.get(url)

if resposta.status_code == 200:
    piada = resposta.json()
    print(f"{piada['setup']}\n{piada['punchline']}")
else:
    print("Erro ao buscar a piada.")
