entrada1 = list(input().split())

produtos = {}
for i in range(0,len(entrada1),2):
    produtos[entrada1[i]] = float(entrada1[i+1])

valor_final = 0

entrada2 = list(input().split())

itens = {}
for i in range(0,len(entrada2),2):
    itens[entrada2[i]] = int(entrada2[i+1])

for item in itens:
    if item in produtos:
        valor_final += (itens[item] * produtos[item])

print(f'R$ {valor_final:.2f}')