salario = float(input('Qual é o seu salário? '))
if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem ganhava R$ {salario:.2f}, com o aumento ganhará R$ {aumento:.2f}.')
