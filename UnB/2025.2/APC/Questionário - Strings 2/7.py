frase1 = 'aaaabc'
frase2 = 'abc'
tam1 = len(frase1)
tam2 = len(frase2)

if tam2 > tam1:
    frase1, frase2 = frase2,frase1
    tam1, tam2 = tam2, tam1

qt_oper1 = 0
qt_oper2 = 0
qt_oper_min = len(frase1) + len(frase2)

for i in range(tam2):
    for j in range(tam2,0+i,-1):
        a = frase2[i:j]
        qt_oper1 = 0
        print('nice')
        for x in range(tam1):
            qt_oper2 = 0
            for y in range(tam1,tam2-i+x-1,-1):
                b = frase1[x:y]
                print(b)
                print(a)
                if a == b:
                    if qt_oper2 + qt_oper1 < qt_oper_min:
                        qt_oper_min = qt_oper2 + qt_oper1
                    
                    print('legal')
            
                qt_oper2 += 1
            qt_oper1 += 1
        qt_oper2 += 1
    qt_oper1 += 1

print(qt_oper_min)



12347
10235