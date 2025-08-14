'''10. Faça um programa para motoristas do Uber que, ao inserir o CEP do endereço do
destino do passageiro ele retorne qual região de São Paulo aquele CEP é. Utilize a
documentação: https://viacep.com.br/
Exemplo: ao inserir o CEP 02122-050 o resultado deve ser a mensagem: Bairro: Vila Maria
Alta, Zona Norte de São Paulo.
As zonas de São Paulo são: Norte, Sul, Leste, Oeste e Centro (indique também quando o
destino da corrida é pra fora da grande são paulo, em cidades vizinhas). Esse programa
será muito útil em relação à segurança dos motoristas, e com ele eles irão poder escolher
pra qual destino querem ou não aceitar corridas.'''

import requests
cep = input("informe o cep: ")
url = f"https://viacep.com.br/ws/{cep}/json"

resp = requests.get(url)

regiao = ""
area = int(cep[:5])

#definir regiao
#https://ricardotrevisan.com/2016/05/03/como-sao-distribuidos-os-ceps-de-sao-paulo/
if area < 1600:
    regiao = "Centro"
elif area < 3000:
    regiao = "Zona Norte"
elif area < 4000 or area >= 8000:
    regiao = "Zona Leste"
elif area < 4900:
    regiao = "Zona Sul"
elif area < 6000:
    regiao = "Zona Oeste"


if resp.status_code == 200:
    dado = resp.json()
    bairro = dado["bairro"]
    print("Bairro", bairro,",", regiao, "de São Paulo")
    
else:
    print("erro", resp.status_code)