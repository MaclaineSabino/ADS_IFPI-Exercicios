def desconto(valor,percentual):
    valorDescontado = valor - (valor*(percentual/100))

    return "o valor com o desconto é: "+str(valorDescontado)


print(desconto(250,10))
