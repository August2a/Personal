def sla(a):
    s = 0
    if a <= 100:
        s = 1 / a + sla(a+1)

    return s

print(f'{sla(1):.2f}')