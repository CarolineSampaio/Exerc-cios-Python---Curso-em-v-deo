#   Minha solução
print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UM PA'))
print('=' * 30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
contador = 0
continuar = True
while continuar:
    print(f'{termo}', end=' → ')
    termo += razão
    contador += 1
    if contador >= 10 and continuar == 1:
        print('PAUSA')
        continuar = int(input('Deseja ver mais termos? Quantos? ')) + 1
    if contador >= 10 and continuar >= 1:
        continuar -= 1
print(f'A progressão foi finalizada com {contador} termos mostrados.')

#   Solução Professor
# print('=' * 30)
# print('{:^30}'.format('10 TERMOS DE UM PA'))
# print('=' * 30)
# primeiro = int(input('Primeiro termo: '))
# razão = int(input('Razão da PA: '))
# termo = primeiro
# contador = 1
# total = 0
# mais = 10
# while mais != 0:
#     total += mais
#     while contador <= total:
#         print(f'{termo}', end=' → ')
#         termo += razão
#         contador += 1
#     print('PAUSA')
#     mais = int(input('Deseja ver mais termos? Quantos? '))
# print(f'A progressão finalizada com {total} termos mostrados.')
