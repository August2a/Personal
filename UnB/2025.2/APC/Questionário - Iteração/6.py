qt_amigos, preco = list(map(int,input().split()))
dinheiro = 0

for _ in range (qt_amigos):
    dinheiro += int(input())

media = dinheiro / qt_amigos

print(f'media: {int(media)}')

if media >= preco:
    print('o rock reinara mais uma vez')
else:
    print('rockeiros trabalhando ja')