x = input()
palavra = ''

for i in range(len(x)):
    if i % 2 != 0 and x[i] != ' ':
        palavra += x [i]  

print(palavra)