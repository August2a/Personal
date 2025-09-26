quantidade_pares = 0

for i in range(5):
    valor = float(input())

    if valor % 2 == 0:
        quantidade_pares += 1


print(
    f'{quantidade_pares} valores pares'
)