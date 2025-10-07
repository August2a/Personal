qt_doce = int(input())
qt_pessoas = int(input()) + 1

doces_para_cada = qt_doce // qt_pessoas
doces_sobraram = qt_doce % qt_pessoas

print(
    f'{doces_para_cada}\n'
    f'{doces_sobraram}'
)
