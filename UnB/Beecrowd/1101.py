m, n = 1,2

while m > 0 and n > 0:
    sum = 0
    for i in range(n,m+1):
        print(i, end=' ')
        sum += i
    if sum != 0:
        print(f'Sum={sum}')
    m, n = list(map(int,input().split()))
    if n > m:
        m, n = n, m
