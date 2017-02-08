def arrecadacao(QtdPao,QtdBroa):
    valorPao = 0.12
    valorBroa = 1.50
    
    total = (QtdPao*0.12)+(QtdBroa*1.50)
    
    return total


def poupanca(total):
    
    return 0.10*total

def emitirResultados():
    valor = arrecadacao(100,10)
    print('foi arrecadado: '+ str(valor))
    
    print('será depositado na poupanca: '+ str(poupanca(valor)))
    
    
emitirResultados()
    
    


