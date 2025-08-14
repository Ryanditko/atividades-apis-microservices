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