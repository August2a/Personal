notas = list(map(int,input().split()))
tipo_nota = input()
soma_notas = 0

if tipo_nota == 'P':
    pesos = list(map(int,input().split()))
    soma_pesos = 0

    for n, p in  zip(notas,pesos):
        soma_notas += n * p
        soma_pesos += p
    
    media  = soma_notas / soma_pesos
    print(f'Ponderada\n{media:.2f}')

elif tipo_nota == 'H':

    for n in notas:
        soma_notas += (1 / n)
    
    media = len(notas) / soma_notas
    print(f'Harmonica\n{media:.2f}')

elif tipo_nota == 'A':
    for n in notas:
        soma_notas += n
    
    media = soma_notas / len(notas) 
    print(f'Aritmetica\n{media:.2f}')

else:
    print('Operacao inexistente')