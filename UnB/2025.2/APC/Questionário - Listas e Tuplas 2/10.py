qt_item_lista = int(input())

lista = [[],[]]
for _ in range(qt_item_lista):
    produto, quantidade = input().split()
    quantidade = int(quantidade)
    
    lista[0].append(produto)
    lista[1].append(quantidade)

qt_item_mercado = int(input())

mercado = [[],[]]
for _ in range(qt_item_mercado):
    produto, preco = input().split()
    preco = float(preco)
    
    mercado[0].append(produto)
    mercado[1].append(preco)

valor_total = 0
for i in range(qt_item_lista):
    if lista[0][i] in mercado[0]:
        index_produto = mercado[0].index(lista[0][i])
        
        valor_produto = mercado[1][index_produto] 
        qt_produto = lista[1][i] 
        
        valor_total += valor_produto * qt_produto
    else:
        print(f'{lista[0][i]} esta em falta')

print(f'{valor_total:.2f}')
        