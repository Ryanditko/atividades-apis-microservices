"""3. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:

1

Atividade de Revisão em Python - IMPACTA
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero e
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for
D ou E."""

# notas parciais
nota_parcial1 = float(input("digite sua nota parcial numero um:"))
nota_parcial2 = float(input("digite sua nota parcial numero dois:"))
media_final = (nota_parcial1 + nota_parcial2)/2

# calculando se o aluno foi APROVADO OU REPROVADO
def calculadora_de_notas():
    if media_final >= 9.0 and media_final <= 10.0:
        print("Voce recebeu nota A")
        print("APROVADO", media_final)
    
    if media_final >= 7.5 and media_final < 9.0:
        print("Voce recebeu nota B")
        print("APROVADO", media_final)

    if media_final >= 6.0 and media_final < 7.5:
        print("Voce recebeu nota C")
        print("APROVADO", media_final)

    if media_final >= 4.0 and media_final < 6.0:
        print("Voce recebeu nota D")
        print("REPROVADO", media_final)

    if media_final < 4.0 and media_final >= 0:
        print("Voce recebeu nota E")
        print("REPROVADO", media_final)

calculadora_de_notas()