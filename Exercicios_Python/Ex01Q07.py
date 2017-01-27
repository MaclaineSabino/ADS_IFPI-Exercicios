def totalLitros():
    formato1 = int(input('quantos refrigerantes de 350ml: '))
    formato2 = int(input('quantos refrigerantes de 600ml: '))
    formato3 = int(input('quantos refrigerantes de 2L: '))
     
    litros = formato1*350/1000 + formato2*600/1000 + 2*formato3
    
    print('o total de litros comprados: '+str(litros)+'L')
    
    
totalLitros()