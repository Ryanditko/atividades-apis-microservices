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