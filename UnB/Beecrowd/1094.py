qt_entradas =int(input())
qt_coelho, qt_rato, qt_sapo = 0, 0, 0
qt_total = 0

for _ in range(qt_entradas):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)

    qt_total += quantidade
    if tipo == 'C':
        qt_coelho += quantidade
    
    elif tipo == 'R':
        qt_rato += quantidade
    
    elif tipo == 'S':
        qt_sapo += quantidade
    
print(
    f'Total: {qt_total} cobaias\n'
    f'Total de coelhos: {qt_coelho}\n'
    f'Total de ratos: {qt_rato}\n'
    f'Total de sapos: {qt_sapo}\n'
    f'Percentual de coelhos: {((qt_coelho / qt_total) * 100):.2f} %\n'
    f'Percentual de ratos: {((qt_rato / qt_total) * 100):.2f} %\n'
    f'Percentual de sapos: {((qt_sapo / qt_total) * 100):.2f} %'
)