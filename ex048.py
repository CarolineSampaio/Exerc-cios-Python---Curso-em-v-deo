soma = 0
cont = 0
for number in range(1, 500, 2):
    if number % 3 == 0:
        cont += 1
        soma += number
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
