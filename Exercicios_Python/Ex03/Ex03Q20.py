def indiceMassa(massa,altura):

    valor = massa/(altura*altura)
    if valor<18.5:
        return 'Abaixo do peso'
    elif valor<25:
        return 'Peso normal'
    elif valor<30:
        return 'Sobrepeso'
    elif valor<35:
        return 'Obeso leve'
    elif valor<40:
        return 'Obeso moderado'
    elif valor>=40:
        return 'Obeso mórbido'


def entradaValores():
    v1 = float(input('Entre com sua massa em kilogramas: '))
    v2= float(input('Entre com sua altura em metros: '))
    return indiceMassa(v1,v2)

print(entradaValores())
