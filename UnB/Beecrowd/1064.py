soma_valores = 0
quantidade_positivos = 0

for i in range(6):
    valor = float(input())

    if valor >= 0:
        soma_valores += valor
        quantidade_positivos += 1

media = soma_valores / quantidade_positivos

print(
    f'{quantidade_positivos} valores positivos\n' + 
    f'{media:.1f}'
)