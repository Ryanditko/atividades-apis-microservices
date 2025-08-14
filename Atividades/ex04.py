'''4. Desenvolver um programa para verificar a nota dos alunos em uma prova com 10
questões. O programa deve seguir os seguintes passos:
• Perguntar ao aluno a resposta de cada uma das 10 questões.
• Comparar as respostas fornecidas pelo aluno com o gabarito da prova.
• Calcular o total de acertos, atribuindo 1 ponto para cada resposta correta.
• Após cada aluno utilizar o sistema, perguntar se outro aluno deseja fazer a prova.
Após todos os alunos terem respondido, o programa deve informar:
• O maior e o menor número de acertos entre os alunos.
• O total de alunos que utilizaram o sistema.
• A média das notas da turma.'''

def gabarito_provas():
    gabarito = []
    for i in range(10):
        resposta = input(f"Digite a resposta da questão {i + 1}: ")
        gabarito.append(resposta)
    return gabarito

def corrigir_prova(gabarito, respostas_aluno):
    acertos = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            acertos += 1
    return acertos


gabarito = gabarito_provas()
resultados = []

while True:
    respostas_aluno = []
    print("\nResponda as 10 questões:")
    for i in range(10):
        resposta = input(f"Resposta da questão {i + 1}: ")
        respostas_aluno.append(resposta)
    acertos = corrigir_prova(gabarito, respostas_aluno)
    print(f"Você acertou {acertos} questões.")
    resultados.append(acertos)
    continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").strip().lower()
    if continuar != 's':
        break

if resultados:
    maior = max(resultados)
    menor = min(resultados)
    total = len(resultados)
    media = sum(resultados) / total
    print(f"\nMaior número de acertos: {maior}")
    print(f"Menor número de acertos: {menor}")
    print(f"Total de alunos: {total}")
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhum aluno respondeu a prova.")