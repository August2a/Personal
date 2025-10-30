def tem_letra_maiúscula(s):
    achou = False
    for letra in s:
        if letra.isupper():
            achou = letra.isupper()
    return achou