qt_notas_validas = 0
soma = 0

while qt_notas_validas < 2:
    nota = float(input())

    if nota >= 0 and nota <= 10:
        qt_notas_validas += 1
        soma += nota
    else:
        print('nota invalida')

print(f'media = {(soma / 2):.2f}')
