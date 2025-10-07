n = int(input())

a, b = 0, 1
numeros = ''

for _ in range(n):
    numeros += str(a) + ' '
    a, b = b, a + b

numeros = numeros.strip()
print(numeros)