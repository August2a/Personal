qt_casos = int(input())

for _ in range(qt_casos):
    cifra = input()
    ajuste = int(input())
    msg = ''

    for i in range(len(cifra)):
        letra = ord(cifra[i]) - ajuste

        if letra < ord('A'):
            letra = (ord('Z') - (ord('A') - letra)) + 1
        
        msg = msg + chr(letra)
    
    print(msg)