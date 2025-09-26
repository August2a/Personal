nome = 'Não tem'
contador = -1
salario = 9999999999.99
menor_salario = [nome,salario]

while nome.lower() != 'fim':
    contador += 1
    
    if salario < menor_salario[1]:
        menor_salario[1] = salario
        menor_salario[0] = nome

    nome, salario = input().split(',')
    salario = float(salario)

print(menor_salario[0])