def troco(x):
    cinquenta = x // 50
    x = x % 50
    vinte_cinco = x // 25
    x = x % 25
    dez = x // 10
    x = x % 10
    cinco = x // 5
    x = x % 5
    um = x // 1
    
    print(
        f'{cinquenta} moedas de 50 centavos\n' + 
        f'{vinte_cinco} moedas de 25 centavos\n' + 
        f'{dez} moedas de 10 centavos\n' + 
        f'{cinco} moedas de cinco centavos\n' + 
        f'{um} moedas de 1 centavo'
    )