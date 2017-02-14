def resultado(b):
    if((b%2==0) and (b%3==0)):
        return 'Verdadeiro'
    else:
        return ' '


valor = int(input('Digite um número: '))

print(resultado(valor))
