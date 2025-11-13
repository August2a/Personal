grade = []
qt_dias = 6                 # Seg, Ter, Qua, Qui, Sex, Sab
qt_horarios = 15            # 5 horários possíveis de manhã e 6 a tarde e 4 noite
impri_linha = ('+---------------+----------+----------+----------+----------+----------+----------+')
impri_dias = ('|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |')
impri_horas = [
    '08:00 - 08:55',
    '08:55 - 09:50',
    '10:00 - 10:55',
    '10:55 - 11:50',
    '12:00 - 12:55',
    '12:55 - 13:50',
    '14:00 - 14:55',
    '14:55 - 15:50',
    '16:00 - 16:55',
    '16:55 - 17:50',
    '18:00 - 18:55',
    '19:00 - 19:50',
    '19:50 - 20:40',
    '20:50 - 21:40',
    '21:40 - 22:30',
]
impri_cod_branco = ('        ')
def tradutor_dth(dth):
    turno = ''
    for caractere in dth:
        if caractere.isalpha():
            turno = caractere
    
    dias,horarios = dth.split(turno)

    index_dias = []
    for dia in dias:
        index_dias.append(int(dia)-2)

    x = 0
    if turno == 'M':
        x = -1
    elif turno == 'T':
        x = 4
    elif turno == 'N':
        x = 10

    index_horarios = []
    for hora in horarios:
        index_horarios.append(int(hora)+x)


    return index_dias,index_horarios 
def gera_grade_vazia():
    for i in range(qt_horarios):
        dia = []
        for j in range(qt_dias):
            dia.append(0)
        grade.append(dia)
def adiciona_na_grade(cod,dth):
    index_dias,index_horarios = tradutor_dth(dth)
    
    for dia in index_dias:
        for hora in index_horarios:
            if grade[hora][dia] != 0:   # ja tem alguma materia nesse dia e horario ? 
                return False            # se sim retorna false 
            
    for dia in index_dias:              # se estiver livre adiciona a materia 
        for hora in index_horarios:
            grade[hora][dia] = cod
    return True
def remove_na_grade(cod,dth):
    index_dias,index_horarios = tradutor_dth(dth)

    for dia in index_dias:
        for hora in index_horarios:
            if grade[hora][dia] != cod: # tem a materia nesse dia e horario ? 
                return False            # se não retorna false
    
    for dia in index_dias:              # se a materia está na grade remove ela 
        for hora in index_horarios:
            grade[hora][dia] = 0
    
    return True
def imprime_grade():
    print(impri_linha)
    print(impri_dias)
    print(impri_linha)


    for hora in range(qt_horarios):
        tem_materia = False
        for dia in range(qt_dias):
            if grade[hora][dia] != 0:
                tem_materia = True
        
        if tem_materia:
            print(f'| {impri_horas[hora]} ',end='')

            for materia in grade[hora]:
                if materia != 0:
                    print(f'| {materia} ',end='')
                else:
                    print(f'| {impri_cod_branco} ',end='')
                
            print('|')
            print(impri_linha)

gera_grade_vazia()
frase_final = 'Hasta la vista, beibe!'
entrada = input()
while entrada != frase_final:
    if entrada == '?':
        imprime_grade()
    else:
        lista_entrada = entrada.split()
        opr, cod, dia_hora = lista_entrada[0],lista_entrada[1],lista_entrada[2:len(lista_entrada)]

        for dth in dia_hora:
            if opr == '+':
                retorno = adiciona_na_grade(cod,dth)
                if retorno == False:
                    print(f'!({entrada})')
                    break

            elif opr == '-':
                retorno = remove_na_grade(cod,dth)
                if retorno == False:
                    print(f'!({entrada})')
                    break
    
    entrada = input()