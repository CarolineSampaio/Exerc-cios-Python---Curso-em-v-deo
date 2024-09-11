"""Crie um programa que leia vários números e coloque em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre as três listas geradas."""

valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um número inteiro: ')))
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Os valores digitados foram {valores}')
print(f'Os valores pares digitados foram {sorted(pares)}')
print(f'Os valores impares digitados foram {sorted(impares)}')
