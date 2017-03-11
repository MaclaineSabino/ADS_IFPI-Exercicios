def potencia(base,expoente):
    valorBase = base
    if(base>=2 and expoente>1 and isinstance(base,int)):
        for i in range(expoente-1):
            base*=valorBase

        print(base)
    else:
        print('a base tem que ser inteira e maior que 2 e o expoente tem que ser maior que 1 e inteiro')




potencia(2,10)

