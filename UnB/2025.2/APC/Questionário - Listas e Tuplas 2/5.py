qt = int(input())
n = int(input())

matriz = []
for i in range(qt):
    lista = list(map(int,input().split()))
    
    matriz.append(lista)

for i in range(qt):
    for j in range(qt-i-1): # -i para diminuir a lista a cada interação
        if matriz[j][n] > matriz[j+1][n]: # se o n-ésimo termo é maior que o proximo n-ésimo termo 
            matriz[j],matriz[j+1] = matriz[j+1],matriz[j]   # trocar de lugar
        elif matriz[j][n] == matriz[j+1][n]:  # se o n-ésimo termo é igual ao proximo n-ésimo termo 
            if sum(matriz[j]) > sum(matriz[j+1]): # e a soma da lista atual é maior que a soma da proxima
                matriz[j],matriz[j+1] = matriz[j+1],matriz[j] # trocar de lugar

for item in matriz:
    print(*item)