salario1=float(input('Qual é o salario do funcionario? R$'))
aumento=float(salario1*15/100)
salario2=float(salario1+aumento)
print('Um funcionario que ganhava R$ {}, com 15% de aumento, passa a receber R${}'.format(salario1,salario2))