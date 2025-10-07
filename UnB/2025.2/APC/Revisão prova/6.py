n = int(input())
divisor = 0
maior_qt_divisores = 0

for i in range(1,n+1):
    qt_divisores = 0

    for j in range(1,i+1):
        if i % j == 0:
            qt_divisores += 1
    
    if qt_divisores > maior_qt_divisores:
        maior_qt_divisores = qt_divisores
        divisor = i

print(divisor,maior_qt_divisores)
