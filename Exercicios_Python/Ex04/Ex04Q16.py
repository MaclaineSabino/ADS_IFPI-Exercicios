from random import randint
lista=[]


countPar=0
countImpar=0
for i in range(0,200):
    lista.append(randint(1,100000))

for a in lista:
    if(a%2==0):
        countPar=countPar+1
    else:
        countImpar=countImpar=countImpar+1

print("Quantidade de pares: "+(str)(countPar))
print("Quantidade de pares: "+(str)(countImpar))
