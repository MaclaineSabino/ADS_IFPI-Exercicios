def totalCofre():
    umc = int(input('digite a quantidade de moedas de 1 centavo: '))
    cincoc = int(input('digite a quantidade de moedas de 5 centavos: '))
    dezc = int(input('digite a quantidade de moedas de 10 centavos: '))
    vintecincoc = int(input('digite a quantidade de moedas de 25 centavos: '))
    cinquentac = int(input('digite a quantidade de moedas de 50 centavos: '))
    umreal = int(input('digite a quantidade de moedas de 1 real: '))
    
    total = (umc*1+cincoc*5+dezc*10+vintecincoc*25+cinquentac*50)/100+umreal
    
    print('o cofre tem um total de: '+str(total)+' reais')
    
totalCofre()
    
    