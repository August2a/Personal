senha = input()
upper = False
number = False
alfa_num_len = False

if senha.isalnum() and (len(senha) >= 6 and len(senha) <= 32):
    alfa_num_len = True
    for letra in senha: 
        if letra.isupper():
            upper = True
        if letra.isnumeric():
            number = True

if upper and number and alfa_num_len:
    print('Senha valida.')
else:
    print('Senha invalida.')