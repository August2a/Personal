lista =[]
def fibonacci(n):
    if n == 0:
        valor = 0
    elif n == 1:
        valor = 1
    else:
        valor = fibonacci(n-2) + fibonacci(n-1)
    
    lista.append(n)
    return valor

n = int(input())
print(f'Termo: {fibonacci(n)}')
print('Quantidades:')
for i in range(n+1):
    print(f'fibonacci({i}) - {lista.count(i)}')
    