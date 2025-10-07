texto = input()
palavra = input()

if palavra in texto:
    texto = texto.replace(palavra,'*')
else:
    texto = 'tudo certo :)'

print(texto)