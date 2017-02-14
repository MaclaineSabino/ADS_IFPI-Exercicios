def multiploSete(b):
    if b%7==0:
        return 'Número múltiplo de 7'
    else:
        return 'Número não múltiplo de 7'



valor = int(input('Digite um número: '))

print(multiploSete(valor))
