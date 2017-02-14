def termomentro(b):
    if b<36.5:
        return 'Está sem febre'
    else:
        return 'Está com febre'


temper = float(input('digite a sua temperatura córporea: '))

print(termomentro(temper))
