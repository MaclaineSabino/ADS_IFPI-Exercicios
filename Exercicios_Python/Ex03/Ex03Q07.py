def saudacao(nome,sexo):
    if sexo=='M':
        return "Ilmo.Sr "+str(nome)
    elif sexo=='F':
        return "Ilmo.Sra "+str(nome)

    else:
        return "Os dados informados estão incorretos, verifique se o sexo está com letra maiúscula"


def entradaValores():
    nome = input("informe seu nome: ")
    sexo = input("informe seu sexo M - Masculino F - Feminino")

    return saudacao(nome,sexo)

print(entradaValores())
