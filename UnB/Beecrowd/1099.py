qt_casos = int(input())
for _ in range(qt_casos):
    x, y = list(map(int,input().split()))

    if y > x:
        x, y = y, x
    
    soma = 0
    for i in range(1,x-y):
        if (y + i) % 2 != 0:
            soma += y + i
    
    print(soma)
