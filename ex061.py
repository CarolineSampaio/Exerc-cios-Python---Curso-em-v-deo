print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UM PA'))
print('=' * 30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
contador = 1
while contador <= 10:
    print(f'{termo}', end=' → ')
    termo += razão
    contador += 1
print('FIM')
