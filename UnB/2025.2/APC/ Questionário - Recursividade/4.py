def controle(n,c):
    c += 1
    if n == c:
        print(f'Parabens Julie! Voce tomou todos os {n} comprimidos!')
    else:
        print(f'Voce ja tomou {c} comprimidos, restam {n-c}.')
        controle(n,c)