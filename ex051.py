print('='*30)
print('{:^30}'.format('10 TERMOS DE UM PA'))
print('='*30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = termo + (10 - 1) * razão
for termos in range(termo, decimo + razão, razão):
    print(termos, end=' → ')
print('Acabou')
