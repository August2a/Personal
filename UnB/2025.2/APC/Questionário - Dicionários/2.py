qt_alunos = int(input())

dic = {}
for _ in range(qt_alunos):
    aluno, nota = input().split(', ')
    nota = float(nota)
    
    if nota in dic:
        dic[nota].append(aluno)
    else:
        dic[nota] = [aluno]

sua_nota = float(input())

if sua_nota in dic:
    dic[sua_nota].sort()
    print(*dic[sua_nota],sep='/')
else:
    print('Você foi o único aluno com essa nota.')