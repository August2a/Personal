numeros = ['one', 'two', 'three']

qt_casos = int(input())

for _ in range(qt_casos):
    entrada = input()
    saida = 0
    for i in range(len(numeros)):
        matchs = 0
    
        if len(entrada) == len(numeros[i]):
            for j in range(len(entrada)):
                if entrada[j] == numeros[i][j]:
                    matchs += 1

        if matchs >= len(numeros[i]) - 1:
            saida = i + 1

    print(saida)
    