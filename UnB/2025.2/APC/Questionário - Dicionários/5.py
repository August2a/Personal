n = int(input())

mercado = {}
for i in range(n):
    entrada = input().split()
    produtos = {}
    for j in range(0,len(entrada),2):
        produtos[entrada[j]] = float(entrada[j+1])
    
    mercado[i+1] = produtos

corredor = int(input())

if corredor in mercado:
    lista =[]
    preco = 0
    for produto in mercado[corredor]:
        lista.append(produto)
        preco += mercado[corredor][produto]

    media = preco / len(lista)
    print(f'No corredor {corredor} encontramos:')
    print(*lista,sep=', ')
    print(f'E o preço médio é {media:.2f}.')
else:
    print(f'Esse corredor não existe no mercado.')