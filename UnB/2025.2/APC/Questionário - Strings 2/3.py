def não_possui_a_letra_u(palavra):
    for letra in palavra:
        if letra.lower() in 'uüúûũù':
            return False
    return True