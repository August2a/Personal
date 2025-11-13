n = int(input())

matriz = []
for _ in range(n):
    lista = input().split()
    
    matriz.append(lista)

valida = True
for i in range(n):
    for j in range(n):
        if j == 0+i or j == n-i-1:
            if matriz[i][j] != 'X':
                valida = False
        elif matriz[i][j] == 'X':
            valida = False

if valida:
    print('O one piece eh real!')
else:
    print('Talvez o tesouro seja os amigos que fizemos no caminho')