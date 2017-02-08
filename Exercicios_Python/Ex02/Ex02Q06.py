def conversorVelocidade(b):
    vMetrosPorSegundo = b/3.6

    return str(b)+" km/h é o equivalente a "+str(vMetrosPorSegundo)+" m/s"


print(conversorVelocidade(72))
