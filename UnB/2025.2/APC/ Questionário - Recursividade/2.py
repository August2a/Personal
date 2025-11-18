def fibonacci(n):
    cache = {}
    def fibonacci_re(n):
        if n in cache:
            return cache[n]

        if n == 1:
            valor = 0
        elif n == 2:
            valor = fibonacci_re(n-1) + 1
        else:
            valor = fibonacci_re(n-1) + fibonacci_re(n-2)
        
        cache[n] = valor
        return valor
    fibonacci_re(n)
    for i in cache:
        print(cache[i],end=' ')
    print('')