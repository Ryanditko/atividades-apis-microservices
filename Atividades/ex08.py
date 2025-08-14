'''8. Faça chamada à API restcountries, que retorna informações sobre países, extraia essas
informações para as manipular conforme orientações abaixo. Por exemplo, ao acessar

https://restcountries.com/v3.1/name/brazil, onde brazil é o país escolhido, é retor-
nado em JSON vários dados sobre o Brasil, em posse disso você deve exibir no programa

que criará:
• Nome do país (Brasil), linguagem(s) (“Portuguese”...), região (“Americas”), subregião
(“South America”) com a capital (“Brasilia”)
• Sigla da moeda (BRL), nome (“Brazilian real”) e símbolo da moeda (“R$”)
• Países que fazem fronteira com o Brasil: “ARG”, “BOL”, “COL”, “GUF”, “GUY” ...
Permita que o usuário insira o nome do país (ex: italy, zambia, japan, canada, germany) e
são retornados esses dados.'''

import requests

pais = input("Digite um pais (Grafia inglesa): ")
url = f"https://restcountries.com/v3.1/name/{pais}"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print("Nome do Pais: ", dados[0]["name"]["common"])
   
    print("Capital(is) do pais: ", end=" ")
    for cap in dados[0]["capital"]:
        print(cap, end=", ")
    print("")
    print("Regiao: ",dados[0]["region"])
    print("Subregiao: ",dados[0]["subregion"])
    print("lingua(s) do pais: ", end=" ")
    for lang in dados[0]["languages"]:
        print(lang, end=", ")
    print(" ")
    sigla = dados[0]["currencies"].keys()
    for sig in sigla:
        print("Simbolo da moeda: ", dados[0]["currencies"][sig]["symbol"])
        print("nome da moeda: ", dados[0]["currencies"][sig]["name"])
        print("Sigla: ", sig)
        
    print("Faz fronteira com: ", end=" ")
    for fronteira in dados[0]["borders"]:
        print(fronteira, end=", ")
        
    
    
else:
    print("erro ", response.status_code)