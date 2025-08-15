'''2. Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a
valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas
disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes
na máquina.
• Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
• Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma
nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

valor = int(input("Digite a valor do saque: "))

# definindo se o valor é valido
if valor >= 10 and valor <= 600:
    total = valor

    # verificando as notas de 100
    if valor >= 100:
        if valor%100 == 0:
            notas_100 = valor/100
            total -= valor
        if valor%100 > 0:
            notas_100 = valor//100
            total -= notas_100*100
    else:
        notas_100 = 0

    # verificando as notas de 50
    if total >= 50:
        if total%50 == 0:
            notas_50 = total/50
            total -= total
        if total%50 > 0:
            notas_50 = total//50
            total -= notas_50*50
    else:
        notas_50 = 0

    # verificando as notas de 10
    if total >= 10:
        if total%10 == 0:
            notas_10 = total/10
            total -= total
        if total%10 > 0:
            notas_10 = total//10
            total -= notas_10*10
    else:
        notas_10 = 0

    # verificando as notas de 5
    if total >= 5:
        if total%5 == 0:
            notas_5 = total/5
            total -= total
        if total%5 > 0 and total >= 1:
            notas_5 = total//5
            total -= notas_5*5
    else:
        notas_5 = 0

    # verificando as notas de 1
    if total%1 == 0:
        notas_1 = total
        total -= total
    print(f'Notas de 100: {notas_100}\n Notas de 50: {notas_50}\n Notas de 10: {notas_10}\n Notas de 5: {notas_5}\n Notas de 1: {notas_1}')
else:
    print('Valor inválido!')
