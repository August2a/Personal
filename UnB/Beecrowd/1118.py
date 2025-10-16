continua = True
entrada = ''
while continua: 
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

    while entrada != '1' and entrada != '2':
        print('novo calculo (1-sim 2-nao)')
        entrada = input() 
    
    if entrada == '2' :
        continua = False
    else:
        entrada = ''
