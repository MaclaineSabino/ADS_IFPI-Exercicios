def semaforo(b):
    if(b=='E'):
        return 'Pare'
    elif(b=='V'):
        return 'Siga'
    elif(b=='A'):
        return 'Atenção'
    else:
        return 'Informação inválida'



def entradas():
    valor = input('digite uma letra de acordo com o sinal: V - Verde, A - Amarelo, E - Veremlho ')
    s = valor.upper()

    return semaforo(s)


print(entradas())

