num = int(input('Digite o número inteiro que deseja converter: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL)''')
conv_tipo = int(input('Sua opção: '))
if conv_tipo == 1:
    print(f'O número {num} convertido para BINÁRIO é igual a {format(num, "b")}.')
elif conv_tipo == 2:
    print(f'O número {num} convertido para OCTAL é igual a {format(num, "o")}.')
elif conv_tipo == 3:
    print(f'O número {num} convertido para HEXADECIMAL é igual a {format(num, "x")}.')
else:
    print('Opção inválida. Tente novamente.')
