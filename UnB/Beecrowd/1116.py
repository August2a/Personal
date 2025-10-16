qt_casos = int(input())

for _ in range(qt_casos):
    x, y = list(map(int,input().split()))

    if y == 0:
        print('divisao impossivel')
    else: 
        print(f'{(x/y):.1f}')