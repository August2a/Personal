x = int(input())
nomes = []

for _ in range(x):
    nomes.append(input())

impostores = input().split()
if impostores != '':
    for impostor in impostores:
        while impostor in nomes:
            nomes.remove(impostor)

print(*nomes)
    
    