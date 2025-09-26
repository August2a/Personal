nome = ' '
contador = -1
maior_salario = 0.0
salario = 0.0

while nome.lower() != 'fim':
    contador += 1
    
    if salario > maior_salario:
        maior_salario = salario

    nome, salario = input().split(',')
    salario = float(salario)

if contador == 0:
    print('Não tem')
else:
    print(f'{maior_salario:.2f}')