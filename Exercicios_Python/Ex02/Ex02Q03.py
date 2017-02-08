def conversorTempo(b):
    hora = int(b/60);
    min = b%60

    return str(hora)+" hora(s) e "+str(min)+" minutos";


print(conversorTempo(2020))

