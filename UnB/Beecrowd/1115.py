x, y = list(map(int,input().split()))
while x != 0 and y != 0:
    if x > 0 and y > 0:
        quadrante = 'primeiro'

    elif x > 0 and y < 0:
        quadrante = 'quarto'

    elif x < 0 and y < 0:
        quadrante = 'terceiro'

    elif x < 0 and y > 0:
        quadrante = 'segundo'
    
    print(quadrante)

    x, y = list(map(int,input().split()))