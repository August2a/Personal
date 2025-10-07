numeros = [
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove'
    ]
    
texto = input()

for i in range(len(numeros)):
    if  numeros[i] in texto:
        texto = texto.replace(numeros[i],str(i))

print(texto)