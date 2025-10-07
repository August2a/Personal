lista_notas = list(map(float,input().split()))
lista_pesos = list(map(int,input().split()))
soma_notas = 0
soma_pesos = 0

for nota, peso in zip(lista_notas,lista_pesos):
    soma_notas += nota * peso
    soma_pesos += peso

media  = soma_notas / soma_pesos

print(f'{media:.6f}')
