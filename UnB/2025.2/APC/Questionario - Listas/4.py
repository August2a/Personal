lista = list(map(int,input().split()))

soma = lista[0] 
lista.pop(0)
for valor in lista:
    soma = soma * 2 + valor * 0.5
print(soma)