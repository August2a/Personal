frase = input().lower()
correcao = 'oi   sbt p'

for i in range(len(correcao)):
    if str(i) in frase:
        frase = frase.replace(str(i), correcao[i])

if frase[len(frase)-1] != '.':
    frase += '.'

frase = frase[0].upper() + frase[1:len(frase)]

print(frase)
    