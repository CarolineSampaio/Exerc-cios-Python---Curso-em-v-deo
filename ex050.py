soma = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i} número: '))
    if numero % 2 == 0:
        soma += numero
print(f'O resultado da soma dos números pares é {soma}.')
