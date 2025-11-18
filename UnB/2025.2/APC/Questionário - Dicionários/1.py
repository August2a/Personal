entrada = input()

teste = {
    'd': 0,
    't': 0,
    'v': 0
}

for i in teste:
    teste[i] = entrada.count(i)

    if teste[i] > 0:
        print(i,teste[i])