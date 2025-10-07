qt_entradas, lotacao_maxima = list(map(int,input().split()))
lotacao = 0
lotou = 'nao'

for i in range(qt_entradas):
    s, e = list(map(int,input().split()))

    lotacao += - s
    lotacao += + e

    if lotacao > lotacao_maxima:
        lotou = 'sim'

print(lotou)