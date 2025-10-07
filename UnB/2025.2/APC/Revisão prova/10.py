tanque_maximo = int(input())
percurso = []

x = 0
while x != -1:
    x = int(input())
    percurso.append(x)

tanque = tanque_maximo
final = 'Lar Deivis lar'
km_atual = 1
i = 0
while i < len(percurso) -1:
    if percurso[i] == 0:
        if tanque - 1 > 0:
            tanque -= 1

        else:
            final = km_atual
            i = len(percurso)

    elif percurso[i] == 1:
        i += 1
        if tanque + percurso[i] <= tanque_maximo:
            tanque += percurso[i]

        else:
            tanque = tanque_maximo

    elif percurso[i] == 2:
        i += 1
        if tanque - percurso[i] > 0:
            tanque -= percurso[i]

        else:
            final = km_atual
            i = len(percurso)

    km_atual += 1
    i += 1

print(final)
