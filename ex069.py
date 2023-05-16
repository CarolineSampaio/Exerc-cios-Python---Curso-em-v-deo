maiores_18 = homens = mulheres_menos_20 = 0
while True:
    print('==' * 14)
    print('{:^28}'.format('CADASTRE UMA PESSOA'))
    print('==' * 14)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'''Total de pessoas com mais de 18 anos: {maiores_18}
Ao todo temos {homens} homens cadastrados
E temos {mulheres_menos_20} mulheres com menos de 20 anos''')
