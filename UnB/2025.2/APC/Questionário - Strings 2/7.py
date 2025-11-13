frase1 = 'helo'
frase2 = 'hello'
#frase1 = input()
#frase2 = input()

tam1 = len(frase1)
tam2 = len(frase2)

if tam2 > tam1:
    frase1, frase2 = frase2,frase1
    tam1, tam2 = tam2, tam1

qt_oper1 = 0
qt_oper1_temp = 0
qt_oper2 = 0
qt_oper2_temp = 0
qt_oper_min = len(frase1) + len(frase2)

for i in range(tam2):
    qt_oper2 = 0
    for j in range(tam2,0+i,-1):
        b = frase2[i:j]
        qt_oper1_temp = 0
        for x in range(tam1):
            qt_oper2_temp = 0
            for y in range(tam1,x+0,-1):
                a = frase1[x:y]
                print(a)
                print(b)
                if a == b:
                    qt_oper_atual = qt_oper2 + qt_oper1 + qt_oper2_temp + qt_oper1_temp
                    if qt_oper_atual < qt_oper_min:
                        qt_oper_min = qt_oper_atual
            
                qt_oper2_temp += 1
            qt_oper1_temp += 1
        qt_oper2 += 1
    qt_oper1 += 1

print(qt_oper_min)