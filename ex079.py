"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos os valores únicos digitados, em ordem crescente."""

lista_num = []

while True:
    num = int(input('Digite um número inteiro: '))
    if num in lista_num:
        print('Número duplicado! Não foi possível adicionar')
    else:
        lista_num.append(num)
        print('Número adicionado com sucesso')
    continuar = input('Deseja continuar? [S/N] ')
    if continuar.upper() == 'N':
        break

print('=-' * 30)
print(f'Você digitou os valores {sorted(lista_num)}')
