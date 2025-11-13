def convert(l):
    
    dicionario = {}
    for tupla in l: 
        if tupla[0] in dicionario:
            dicionario[tupla[0]].append(tupla[1])
        else:
            dicionario[tupla[0]] = [tupla[1]]
    
    return dicionario