def alturaPredio():
    
    sombraPredio = float(input('digite o comprimento da sombra do predio: '))
    sombraPessoa = float(input('digite o comprimento da sombra da pessoa: '))    
    alturaPessoa = float(input('digite a sua altura: '))

    alturaPredio = (sombraPredio/sombraPessoa)*alturaPessoa
    print('a altura do prédio é: '+str(alturaPredio))
    
    
alturaPredio()


