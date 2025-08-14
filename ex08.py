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