n = int(input())

alunos ={}
for _ in range(n):
    entrada = input().split()
    nome,email = entrada[0],entrada[1]
    notas = list(map(float,entrada[2:len(entrada)]))
    
    alunos[nome] = [email,notas]

nome = input()

if nome in alunos:
    print(f'Destinatário: {alunos[nome][0]}')
    situação = ''
    media = sum(alunos[nome][1]) / len(alunos[nome][1])
    if media >= 5:
        situação = 'foi aprovado com média'
    else:
        situação = 'foi reprovado com média'
        
    print(f'O aluno {nome} {situação} {media:.2f}.')
else:
    print(f'O aluno {nome} não está na turma.')