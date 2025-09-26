nome = ' '
media = ' '

soma_salarios = 0

maior_salario = [nome,0,0]
menor_salario = [nome,9999999999.99]

x = int(input())

for _ in range(x):
    nome,salario = input().split(',')

    salario = float(salario)

    soma_salarios += salario

    if salario < menor_salario[1]:
        menor_salario[1] = salario
        menor_salario[0] = nome

    if salario > maior_salario[1]:
        maior_salario[1] = salario
        maior_salario[0] = nome

if x == 0:
    print('Não tem média')
    print('Não tem')
    print('Não tem')

else:    
    media = soma_salarios / x

    print(f'{media:.2f}')
    print(f'{maior_salario[0]} {maior_salario[1]:.2f}')
    print(f'{menor_salario[0]} {menor_salario[1]:.2f}')
