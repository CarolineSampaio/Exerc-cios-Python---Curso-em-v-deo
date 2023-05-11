#   Minha solução
lista = []
for i in range(1, 6):
    peso = float(input(f'Qual é o peso da {i}ª pessoa em kg? '))
    lista.append(peso)
maior = max(lista)
menor = min(lista)
print(f'O maior peso lido foi {maior} kg.\n'
      f'E o menor peso lido foi {menor} kg.')

#   Solução do professor
# maior = 0
# menor = 0
# for p in range(1, 6):
#     peso = float(input(f'Qual é o peso da {p}ª pessoa em kg? '))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f'O maior peso lido foi de {maior} kg.')
# print(f'O menor peso lido foi de {menor} kg.')
