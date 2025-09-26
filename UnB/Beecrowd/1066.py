pares = 0
positivo = 0
negativo = 0

for i in range(5):
    valor = float(input())

    if valor % 2 == 0:
        pares += 1
    
    if valor > 0:
        positivo += 1
    elif valor < 0:
        negativo += 1

print(
    f'{pares} valor(es) par(es)\n' + 
    f'{5 - pares} valor(es) impar(es)\n' + 
    f'{positivo} valor(es) positivo(s)\n' + 
    f'{negativo} valor(es) negativo(s)'
)