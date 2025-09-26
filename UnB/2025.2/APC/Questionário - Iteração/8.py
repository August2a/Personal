pa, pb, t1, t2 = input().split()
pa, pb = int(pa), int(pb)
t1, t2 = float(t1), float(t2)
anos = 0

if t1 - t2 > 0:
    while pa < pb:
        anos += 1
        pa = int(pa * (1+(t1/100)))
        pb = int(pb * (1+(t2/100)))
    
    if anos <= 1000:
        print(f'Vai alcancar em {anos} ano(s).')
    
    else:
        print(f'Mais de um milenio.')

else:
    print('A nunca alcancara B.')