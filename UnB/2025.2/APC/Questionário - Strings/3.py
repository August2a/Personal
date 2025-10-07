x = input()
y = 0

for i in range(len(x)):
    if x[i].isdigit():
        y += 1

print(y)