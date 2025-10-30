entrada = input()
inicio = 0

for i in range(len(entrada)):
    if not(entrada[i].isalpha()):
        print(entrada[inicio:i])
        inicio = i+1

print(entrada[inicio:len(entrada)])