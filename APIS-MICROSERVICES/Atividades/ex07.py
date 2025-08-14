'''7. Faça um programa que leia um número indeterminado de valores numéricos, encerrando
a entrada de dados quando for informado um valor igual a −1 (que não deve ser
armazenado). Após esta entrada de dados, faça:
• Mostre a quantidade de valores que foram lidos;
• Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
• Exiba todos os valores na ordem inversa à que foram informados, um ao lado do outro;
• Calcule e mostre a soma dos valores;
• Calcule e mostre a média dos valores;
• Calcule e mostre a quantidade de valores acima da média calculada;'''

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