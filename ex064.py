#    Minha solução
num = contador = soma = 0
while num != 999:
    num = int(input(f'Digite um número inteiro [999 para parar]: '))
    if num != 999:
        soma += num
        contador += 1
print(f'A soma dos {contador} números digitados é {soma}.')

#   Solução Professor
# contador = soma = 0
# num = int(input(f'Digite um número inteiro [999 para parar]: '))
# while num != 999:
#     soma += num
#     contador += 1
#     num = int(input(f'Digite um número inteiro [999 para parar]: '))
# print(f'A soma dos {contador} números digitados é {soma}.')
