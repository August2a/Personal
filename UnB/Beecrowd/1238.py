qt_casos = int(input())

for _ in range(qt_casos):
    p3 = ''
    p1, p2 = input().split()
    menor_len = min(len(p1), len(p2))

    for i in range(menor_len):
        p3 = p3 + p1[i] + p2[i]

    p3 = p3 + p1[menor_len:] + p2[menor_len:]

    print(p3)
