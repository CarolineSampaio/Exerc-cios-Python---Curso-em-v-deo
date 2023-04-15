salario = float(input('Qual é o salário do Funcionário? R$  '))
salario_final = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario_final:.2f}.')