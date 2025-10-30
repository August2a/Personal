entrada = input()
qt_diferentes = 0

for i in range(len(entrada)):
    if entrada[i] != entrada[len(entrada) - i - 1]:
        qt_diferentes += 1

if qt_diferentes == 2 or (qt_diferentes == 0 and len(entrada) % 2 != 0):
    print('ON')
else:
    print('OFF')
    