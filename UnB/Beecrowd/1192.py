qt_casos = int(input())

for _ in range(qt_casos):
    v1, letra, v2 = list(input())
    v1, v2 = int(v1), int(v2)

    if v1 == v2:
        resultado = v1 * v2
    
    elif letra.isupper():
        resultado = v2 - v1
    
    else:
        resultado = v1 + v2
    
    print(resultado)