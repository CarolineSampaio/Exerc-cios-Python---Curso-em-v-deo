#   Minha solução
continuar = 'S'
contador = 0
lista = []
while continuar in 'Ss':
    num = int(input(f'Digite um número: '))
    lista.append(num)
    contador += 1
    continuar = (input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'SN':
        continuar = 'N'
        print('Opção inválida.')
maior = max(lista)
menor = min(lista)
media = (sum(lista)) / contador

print(f'''
Você digitou {contador} números. A média entre eles é {media:.2f}.
O maior número digitado foi {maior}. O menor número digitado foi {menor}.''')

#   Solução Professor
# resp = 'S'
# soma = quant = media = maior = menor = 0
# while resp in 'Ss':
#     num = int(input(f'Digite um número: '))
#     soma += num
#     quant += 1
#     if quant == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
#     resp = str(input('Deseja continuar? [S/N] '))
# media = soma / quant
# print(f'''
# Você digitou {quant} números. A média entre eles é {media:.2f}.
# O maior número digitado foi {maior}. O menor número digitado foi {menor}.''')
