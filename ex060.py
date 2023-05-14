#   Usando while
num = int(input("Digite um número para calcular o seu Fatorial: "))
fatorial = 1
contador = num
print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(contador, end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)

#   Usando for
# num = int(input("Digite um número para calcular o fatorial: "))
# fatorial = 1
# print(f'Calculando {num}! = ', end='')
# for contador in range(num, 0, -1):
#     print(contador, end='')
#     print(' x ' if contador > 1 else ' = ', end='')
#     fatorial *= contador
# print(fatorial)

# Usando math
# from math import factorial
# num = int(input("Digite um número para calcular o seu Fatorial: "))
# f = factorial(num)
# print(f'O fatorial de {num} é {f}.')
