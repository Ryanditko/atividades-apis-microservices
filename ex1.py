"""1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
• até 20 litros: desconto de 3% por litro
• acima de 20 litros: desconto de 5% por litro
Gasolina:
• até 20 litros: desconto de 4% por litro
• acima de 20 litros: desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado
da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

# definindo as variveis
COMBUSTIVEL = input("Digite A para alcool e G para gasolina:")
QUANTIDADE = int(input("escolha a quantidade desejavel:"))

if COMBUSTIVEL == "A":
    preco = QUANTIDADE * 1.90
    if QUANTIDADE <= 20:
        desconto = preco * 3/100
        valor_a_ser_pago = preco - desconto
        print("voce tem um desconto de 3% por litro")
        print("seu desconto final foi de:", desconto)
        print("o valor final a ser pago foi de:", valor_a_ser_pago)
    else:
        desconto = preco * 5/100
        valor_a_ser_pago = preco - desconto
        print("voce tem um desconto de 5% por litro")
        print("seu desconto final foi de:", desconto)
        print("o valor final a ser pago foi de:", valor_a_ser_pago)


if COMBUSTIVEL == "G":
    preco = QUANTIDADE * 2.50
    if QUANTIDADE <= 20:
        desconto = preco * 4/100
        valor_a_ser_pago = preco - desconto
        print("voce tem um desconto de 4% por litro")
        print("seu desconto final foi de:", desconto)
        print("o valor final a ser pago foi de:", valor_a_ser_pago)
    else:
        desconto = preco * 6/100
        valor_a_ser_pago = preco - desconto
        print("voce tem um desconto de 6% por litro")
        print("seu desconto final foi de:", desconto)
        print("o valor final a ser pago foi de:", valor_a_ser_pago)
