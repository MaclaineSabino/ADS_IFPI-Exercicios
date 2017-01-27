def salario():
    horaNormal = int(input('digite a quantidade de horas normais trabalhadas: '))
    horaExtra = int(input('digite a quantidade de horas extras trabalhadas: '))
    
    total = horaNormal*10 + horaExtra*15
    totalLiquido = 0.9*total
    print('salario liquido do funcionario é: '+ str(totalLiquido))
    
    
    
salario()