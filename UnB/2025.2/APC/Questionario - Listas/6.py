x = int(input())
periodos = []
nome = 'Raimundo Nonato '

for _ in range(x):
    periodos.append(nome + input())

print(*periodos, sep='\n')