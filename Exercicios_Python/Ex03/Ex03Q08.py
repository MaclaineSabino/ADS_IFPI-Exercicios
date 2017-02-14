def resultadoNumero(b):
    if b==0:
        return 'O número informado é zero'
    elif b<0:
        return 'O número informado é negativo'
    else:
        return 'O número informado é positivo'


def entradaValores():
    c = int(input('digite um valor: '))
    return resultadoNumero(c)

print(entradaValores())
