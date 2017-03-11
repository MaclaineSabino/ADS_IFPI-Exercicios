def primo(b):
    cont=0
    for i in range(1,b+1):

        if (b%i)==0:
            cont = cont+1

    if(cont==2):
        print("eh primo")

    else:
        print("não eh primo")


valor = (int)(input('entre com um valor: '))

primo(valor);
