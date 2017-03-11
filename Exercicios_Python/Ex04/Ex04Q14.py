from random import randint
lista=[]

maior=0
for i in range(0,100):
    lista.append(randint(1,100000))

for i in lista:
    if(i>maior):
        maior=i

print(maior)




