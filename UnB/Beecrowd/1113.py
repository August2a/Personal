x, y = 0, 1
while x != y:
    x, y = list(map(int,input().split()))
    
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')