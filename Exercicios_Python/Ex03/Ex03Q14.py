from datetime import date

def podeVotar():
    dataNasc = int(input('Informe seu ano de nascimento: '))
    dataAtual =date.today()
    anoAtual = int(dataAtual.year)

    diferenca = anoAtual-dataNasc
    if(diferenca>=16):
        return 'Pode votar'
    else:
        return 'Não pode votar'


print(podeVotar())

