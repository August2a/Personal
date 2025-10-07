x = input()

i = len(x) - 1

y = x[:2] + x[i-1:i+1]

print(y)