lista_um = []
lista_dois = []
lista_media = []

for _ in range(5):
    lista_um.append(int(input()))

for _ in range(5):
    lista_dois.append(int(input()))

lista_tuple = list(zip(lista_um,lista_dois))

print(lista_tuple)

for elemento in lista_tuple:
    lista_media.append((elemento[0] + elemento[1]) / 2)

print(lista_media)