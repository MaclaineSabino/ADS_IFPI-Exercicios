def retornaResultado(b):
    if (b%5)==0:
        return True
    else:
        return False



d = int(input('digite um número: '))
print(retornaResultado(d))
