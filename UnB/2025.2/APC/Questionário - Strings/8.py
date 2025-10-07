n = int(input())

for _ in range(n):
    entrada = input()
    lista_casos = []
    
    caso = entrada[0]
    for i in range(1,len(entrada)):
        if entrada[i].isdigit():
            caso += entrada[i]
        else:
            lista_casos.append(caso)
            caso = entrada[i]
    lista_casos.append(caso)
    
    saida = ''
    for caso in lista_casos:
        letra = caso[0]
        numero = int(caso[1:len(caso)])
        
        for i in range(numero):
            saida += letra
    
    print(saida)
