def conversorVelocidade(b):
    vKmPorHora=b*3.6;

    return str(b)+" m/s é o equivalente a "+str(vKmPorHora)+" km/h"

print(conversorVelocidade(20))
