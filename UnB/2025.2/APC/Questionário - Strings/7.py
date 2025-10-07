palavra = input()
qt_desiguais = 0
estado = 'OFF'

for i in range(int(len(palavra) / 2)):
    if palavra[i] != palavra[len(palavra) - 1 - i]:
        qt_desiguais += 1

# se for somente 1 caractere desigual, ou se tiver um caractere no meio:
if (qt_desiguais == 0 and len(palavra) % 2 != 0) or (qt_desiguais == 1):
    estado = 'ON'   # muda o estado 

print(estado)