qt_mercearias, mangos, qt_produtos = list(map(int,input().split()))

qt_produto_por_mercearias = list(map(int,input().split()))

e_possivel = True
for i in range(qt_mercearias):
    produtos = list(map(int,input().split()))
    produtos.sort()
    
    if len(produtos) < qt_produtos: 
        e_possivel = False
        break
    else:
        for i in range(qt_produtos):
            mangos -= produtos[i]
            if mangos < 0:
                e_possivel = False
                break

if e_possivel:
    print('Sim')
else:
    print('Nao')