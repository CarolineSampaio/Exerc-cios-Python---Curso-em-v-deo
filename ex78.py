""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista. """

list_num = []

for i in range(5):
    list_num.append(int(input(f'Digite um valor para a posição {i}: ')))

maior = max(list_num)
menor = min(list_num)

posicoes_maior = [i for i, v in enumerate(list_num) if v == maior]
posicoes_menor = [i for i, v in enumerate(list_num) if v == menor]

print('=-' * 30)
print(f'Você digitou os valores {list_num}')
print(f'O maior número digitado foi {maior} nas posições {posicoes_maior}.')
print(f'O menor número digitado foi {menor} nas posições {posicoes_menor}.')
