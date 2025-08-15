'''5. O cardápio de uma lanchonete é o seguinte:
Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule
e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

itens = {100: 1.20,
         101: 1.30,
         102: 1.50,
         103: 1.20,
         104: 1.30,
         105: 1.00}

total_pedido = 0

while True:
    cod = int(input('Digite o código do produto desejado: '))
    qtd = int(input('Qual a quantidade para este produto?: '))
    valor_item = itens[cod] * qtd
    print(f'O valor total para este item é de R${valor_item:.2f}')
    total_pedido += valor_item
    resp = input('Digite 1 para continuar comprando ou outra tecla para encerrar: ')
    if resp == '1':
        continue
    else:
        break
print(f'O valor total da compra foi de R${total_pedido:.2f}')
