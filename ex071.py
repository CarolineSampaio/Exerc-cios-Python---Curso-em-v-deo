#   Otimizado (Com ajuda do professor)
print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)
saque = int(input('Que valor você deseja sacar? R$ '))
total = saque
ced = 50
tot_ced = 0
while True:
    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

#   Primeira Tentativa:
# print('=' * 40)
# print('{:^40}'.format('BANCO CEV'))
# print('=' * 40)
# saque = int(input('Que valor você deseja sacar? R$ '))
# ced_50 = ced_20 = ced_10 = ced_1 = 0
# while True:
#     if saque >= 50:
#         ced_50 = saque // 50
#         saque -= (ced_50 * 50)
#     if saque >= 20:
#         ced_20 = saque // 20
#         saque -= (ced_20 * 20)
#     if saque >= 10:
#         ced_10 = saque // 10
#         saque -= (ced_10 * 10)
#     if saque >= 1:
#         ced_1 = saque
#         saque -= ced_1
#     if saque == 0:
#         break
# if ced_50 > 0:
#     print(f'Total de {ced_50} cédulas de R$ 50')
# if ced_20 > 0:
#     print(f'Total de {ced_20} cédulas de R$ 20')
# if ced_10 > 0:
#     print(f'Total de {ced_10} cédulas de R$ 10')
# if ced_1 > 0:
#     print(f'Total de {ced_1} cédulas de R$ 1')
# print('=' * 40)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
