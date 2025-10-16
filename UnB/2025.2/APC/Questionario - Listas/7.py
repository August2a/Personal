x, y = list(map(int,input().split()))
sala = []

for _ in range(x):
    fileira = list(map(int,input().split()))

    sala.append(fileira)

maior_dis = 0
for fileira in sala:
    for i in range(y):
        if fileira[i] == 0:
            dis_esquerda = 100
            dis_direita = 100

            esquerda = fileira[i::-1]
            if 1 in esquerda:
                dis_esquerda = esquerda.index(1)

            direita = fileira[i:y]
            if 1 in direita:
                dis_direita = direita.index(1) 
            
            menor_dis = min(dis_direita,dis_esquerda)

            if menor_dis > maior_dis:
                maior_dis = menor_dis

print(maior_dis)

