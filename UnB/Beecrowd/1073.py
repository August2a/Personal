nm_casos = int(input())

for i in range(nm_casos):
    valor = int(input())
    
    if valor == 0:
        classificacao = 'NULL'
    else:
        if valor % 2 == 0:
            classificacao = 'EVEN'
        else:
            classificacao = 'ODD'
        
        if valor > 0:
            classificacao += ' POSITIVE'
        else:
            classificacao += ' NEGATIVE'
    
    print(classificacao)