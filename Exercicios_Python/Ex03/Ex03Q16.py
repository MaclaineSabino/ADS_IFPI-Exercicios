def mesAno(b):
    if(b==1):
        return 'janeiro'
    elif(b==2):
        return 'fevereiro'
    elif(b==3):
        return 'março'
    elif(b==4):
        return 'abril'
    elif(b==5):
        return 'maior'
    elif(b==6):
        return 'junho'
    elif(b==7):
        return 'julho'
    elif(b==8):
        return 'agosto'
    elif(b==9):
        return 'setembro'
    elif(b==10):
        return 'outubro'
    elif(b==11):
        return 'novembro'
    elif(b==12):
        return 'dezembro'
    else:
        return 'o valor informado não corresponde a um mês do ano'


valor = int(input('Digite um valor: '))
print(mesAno(valor))
