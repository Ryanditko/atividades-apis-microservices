valor = 0
quantidade = 0
soma = 0
valores = []
while(True):
    valor = int(input("Digite um numero (-1 para sair do programa)"))
    if valor == -1:
        break
    quantidade += 1
    soma += valor
    valores.append(valor)
if quantidade > 0:
    media = soma / quantidade
    print("soma:", soma)
    print("media: ", media)
    maior_que_media = 0
    for v in valores:
        if v >= media:
            maior_que_media += 1
    print("numeros maiores que a media: ", maior_que_media)
else:
    print("quantidade nao pode ser zero")