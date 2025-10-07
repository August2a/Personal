for i in range (0,21):
    if i % 2 == 0:
        for j in range(3):
            z = i / 10
            w = 1 + j + z
            x = str(round(z,10)).rstrip('0').rstrip('.')
            y = str(round(w,10)).rstrip('0').rstrip('.')
            print(f'I={x} J={y}')