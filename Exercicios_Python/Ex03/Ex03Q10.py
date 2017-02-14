def velocidadeMedia(vel,hor):
    velocidadeMedi = vel/hor

    return 'velocidade média é igual a: '+str(velocidadeMedi)+' km/h'


velo = float(input('Digite a velocidade: '))
tempo =float(input('Digite o tempo em horas: '))

print(velocidadeMedia(velo,tempo))
