def contaBar():
    valor = float(input('digite o valor da despesa: '))
    
    carlos = int(valor/3)
    andre = carlos
    felipe = andre + valor%3
    
    print('carlos e andre pagarao: '+str(carlos)+'\n'+'felipe pagará: '+str(felipe))
    
    
   
    
contaBar()