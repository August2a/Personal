def corrida(a,b,c):
    a -= b
    if a <= 0:
        print('A corrida chegou ao fim.')
        return
    else:
        print(f'Faltam {a} voltas, hora de trocar os pneus.')
        b = c
        corrida(a,b,c)
    
corrida(10,3,4)