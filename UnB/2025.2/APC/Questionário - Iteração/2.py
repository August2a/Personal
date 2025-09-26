nome = ' '
contador = -1
salario = 0.0
soma_salarios = 0.0
media = 0.0

while nome.lower() != 'fim':
    contador += 1
    soma_salarios += salario

    nome, salario = input().split(',')
    salario = float(salario)

if contador > 0:
    media = soma_salarios / contador

print(f'{media:.2f}')