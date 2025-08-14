'''9. Neste exercício, você irá criar um programa que solicita ao usuário a sigla de uma moeda
e exibe a cotação do Real (BRL) em relação a essa moeda. O objetivo é fazer uma
requisição à API de cotações de moedas, tratar a resposta e apresentar o valor do Real
em face da moeda escolhida. Você deve usar essa API: https://api.exchangerate-api.
com/v4/latest/BRL onde BRL é a sigla da moeda alvo (Real).
• Solicite ao usuário que insira a sigla da moeda desejada (por exemplo, “USD” para Dólar
Americano, “EUR” para Euro, “GBP” para Libra Esterlina, etc.).
• Faça uma requisição à API de cotações de moedas para obter a taxa de câmbio do Real
em relação à moeda informada pelo usuário.
• Extraia o valor da cotação do Real em relação à moeda solicitada.
• Exiba uma mensagem clara e informativa, como “O Real vale X [nome da moeda]”, onde
X é o valor da cotação. Ex: O Real vale 5.42 dólares americanos, traduzindo a sigla da
moeda para o nome completo (USD para dólares americanos). '''

import requests

#biblioteca para ter o nome da moeda a partir do codigo de 3 digitos
from forex_python.converter import CurrencyCodes

moeda = input("digite a sigla de uma moeda: ").upper()
c = CurrencyCodes()
url = "https://api.exchangerate-api.com/v4/latest/BRL"
resp = requests.get(url)
if resp.status_code == 200:
    dados = resp.json()
    valor = dados["rates"][moeda]
    
    conversao = 1 / valor

    print("O/A", c.get_currency_name(moeda), "equivale a", round(conversao, 2), "reais")
else:
    print("Erro ", resp.status_code)