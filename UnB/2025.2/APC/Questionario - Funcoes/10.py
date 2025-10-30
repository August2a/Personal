def paron(lista):
    vogais = 'aeiou'
    
    for palavra in lista: 
        qt_vogais = 0
        for letra in palavra:
            if letra in vogais:
                qt_vogais += 1
        
        if qt_vogais % 2 != 0:
            lista.remove(palavra)
    
    return lista
    #comece aqui

print(paron(['palavra', 'escrever', 'detesta', 'lista', 'todas']))
