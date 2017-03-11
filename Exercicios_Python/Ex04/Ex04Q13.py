lista = [ ]
soma = 0
contador=0
m = (int)(input('entre com valores inteiros'))

lista.append(m)

while(m!=0):
    m = (int)(input('entre com valores inteiros'))
    lista.append(m)


for i in lista:
    if(i%3==0)and i!=0:
        soma=soma+i
        contador = contador+1

print(soma/contador)






