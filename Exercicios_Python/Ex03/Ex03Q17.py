def respostas(a,b):
    if(a%2==0)and(b%2==0):
        return 'Os dois são pares'
    elif(a%2==0)and(b%2!=0):
        return 'O primeiro é par e o segundo é ímpar'
    elif(a%2!=0)and (b%2==0):
        return 'O primeiro é ímpar e o segundo é par'
    else:
        return "Os dois são ímpares"


def entradaValores():
    v1=int(input('Digite o primeiro valor: '))
    v2=int(input('Digite o segundo valor'))
    return respostas(v1,v2)


print(entradaValores())
