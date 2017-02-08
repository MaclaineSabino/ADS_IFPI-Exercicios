def totalMinutos(b):
    hora=int(b/100)
    minutos=(b%100)
    total=(hora*60)+minutos

    return "total de minutos é: "+str(total)

tempo = int(input("digite a hora no formato HHMM: "))
print(totalMinutos(tempo))

