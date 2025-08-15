'''6. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
• Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
• Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
• A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
o programa permitindo que o usuário digite o salário inicial do funcionário.'''

salario_inicial = float(input("Digite o salário inicial do funcionário: "))
ano_contratacao = 1995
ano_atual = int(input("Digite o ano atual: "))

salario = salario_inicial
percentual = 0.015

salario += salario_inicial * percentual

for ano in range(1997, ano_atual + 1):
    percentual *= 2
    salario += salario * percentual

print(f"O salário atual do funcionário é: R$ {salario:.2f}")
