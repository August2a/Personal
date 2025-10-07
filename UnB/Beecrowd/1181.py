l = int(input())
t = input()

matriz = []
for i in range(12):
    
    linha = []
    for j in range(12):
        linha.append(float(input()))
    
    matriz.append(linha)

saida = 0
for i in range(12):
    saida += matriz[l][i]

if t == 'M': 
    saida = saida / 12

print(f'{saida:.1f}')