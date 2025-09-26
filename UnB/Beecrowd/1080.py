maior_valor = [0,0]

for i in range(100):
    valor = int(input())

    if valor > maior_valor[0]:
        maior_valor = [valor,i+1]

print(maior_valor[0])
print(maior_valor[1])