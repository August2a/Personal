nm_casos = int(input())

dentro = 0
for i in range(nm_casos):
    valor = int(input())

    if 10 <= valor <= 20:
        dentro += 1

print(
    f'{dentro} in\n' +
    f'{nm_casos - dentro} out'
      )