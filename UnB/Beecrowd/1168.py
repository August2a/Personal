valor_numero = [6,2,5,5,4,5,6,3,7,6]

qt_entradas = int(input())

for _ in range(qt_entradas):
    numero = list(map(int,input()))
    
    qt_leds = 0
    for i in numero:
        qt_leds += valor_numero[i]
    
    print(f'{qt_leds} leds')
