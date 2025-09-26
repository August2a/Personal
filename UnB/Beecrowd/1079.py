n = int(input())

for _ in range(n):
    valor = list(map(float,input().split()))
    media  = ((valor[0] * 2) + (valor[1] * 3) + (valor[2] * 5)) / 10

    print(f'{media:.1f}')