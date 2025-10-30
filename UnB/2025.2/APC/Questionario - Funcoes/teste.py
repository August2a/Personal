frase = input().lower()
correcao = 'oi   sbt p'

for i in range(len(correcao)):
    if str(i) in frase:
        frase = frase.replace(str(i), correcao[i])

print(frase)
    



'abcdefg'
'efh'