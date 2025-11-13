# cada jogador é enumerado por um inteiro de 1 a N
# cada equipe é enumerada por um inteiro de 1 a K
# cada empresário é enumerado por um inteiro de 1 a M

# A primeira linha da entrada contém três números inteiros separados 
# por espaço N,M e K
# 10 2 2
# A segunda linha contém N
# inteiros separados por espaço indicando o identificador 
# da equipe defendida pelo i-ésimo atleta
# 1 1 2 2 1 1 2 1 1 2
# A terceira linha contém M inteiros separados por espaço
# representando a quantidade de atletas agenciados 
# pelo j-ésimo empresário
# 5 5
# As próximas M linhas descrevem os atletas agenciados 
# por cada empresário
# 10 6 4 7 1
# 2 9 5 3 8

qt_jogadores, qt_empresários, qt_equipes = list(map(int,input().split()))

jogadores = list(map(int,input().split()))

qt_jogadores_por_empresario = list(map(int,input().split()))

empresarios_culpados =[]
for i in range(qt_empresários):
    atletas_do_empresario = list(map(int,input().split()))
    equipes_empresario_participa = []
    
    for atleta in atletas_do_empresario:
        time_do_atleta = jogadores[atleta-1]
        if time_do_atleta not in equipes_empresario_participa: 
            equipes_empresario_participa.append(time_do_atleta)
    if len(equipes_empresario_participa) == qt_equipes:
        empresarios_culpados.append(i)

if len(empresarios_culpados) == 0:
    print(-1)
else:
    for i in empresarios_culpados:
        print(i+1,end=" ")

