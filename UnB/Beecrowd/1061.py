dia_inicio = int(input().split()[1])
hora_inicio = list(map(int,input().split(' : ')))

dia_final = int(input().split()[1])
hora_final = list(map(int,input().split(' : ')))


segundo_inicial  = (((hora_inicio[0] * 60) + hora_inicio[1]) * 60) + hora_inicio[2]

segundo_final = ((((((dia_final - dia_inicio) * 24) + hora_final[0]) * 60) + hora_final[1]) * 60) + hora_final[2]

segundo_passados = segundo_final - segundo_inicial

dias_passados = segundo_passados // 86400

segundo_passados = segundo_passados % 86400

horas_passadas = segundo_passados // 3600

segundo_passados = segundo_passados % 3600

minutos_passados = segundo_passados // 60

segundos_passados = segundo_passados % 60

print(
    f'{dias_passados} dia(s)\n' + 
    f'{horas_passadas} hora(s)\n' + 
    f'{minutos_passados} minuto(s)\n' + 
    f'{segundos_passados} segundo(s)'
)