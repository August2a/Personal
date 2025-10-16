numeros = list(map(int,input().split()))
n = int(input())

escolhidos = []
for numero in numeros:
    if numero % n == 0:
        escolhidos.append(numero)

print(*escolhidos)