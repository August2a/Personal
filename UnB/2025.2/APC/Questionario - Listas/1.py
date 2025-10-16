x = int (input())
nomes = []

for _ in range(x):
    nomes.append(input())

nomes.reverse()

print(*nomes, sep='\n')