def contagem(n,consegue):
    if n == 0:
        print('Cabum!!!! Explodiu')
        return
    elif n == 1:
        if consegue == True:
            print(f'Seja rápido. Falta {n} segundo')
        else:
            print(f'Bomba desativada automaticamente!')
            return
    elif n == 5:
        print('Seu tempo está acabando!')
    else:
        print(f'Atenção faltam {n} segundos...')
    
    contagem(n-1,consegue)

n = int(input())
p = int(input())
consegue = p < n

contagem(n,consegue)
