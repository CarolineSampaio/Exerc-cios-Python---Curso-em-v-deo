# Solução otimizada após assistir à aula:
idades = 0
media = 0
maior_idade_homem = 0
nome_velho = ''
mulher_menos_20 = 0
for p in range(1, 5):
    print(f'_____ {p}ª PESSOA _____')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idades += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_20 += 1

media = idades / 4
print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulher_menos_20} mulheres com menos de 20 anos.')

# Minha tentativa resolvendo sozinha:
# nomes = []
# idades = []
# sexos = []
# idade_homens = []
# nome_homem = []
# idade_mulheres = []
# mulher_menos_20 = 0
# for dados in range(0, 4):
#     nome = str(input('Digite seu nome: ')).capitalize()
#     idade = int(input('Digite sua idade: '))
#     sexo = str(input('Qual é o seu sexo? [ F ] para feminino e [ M ] para masculino: ')).upper()
#     if sexo != 'M' and sexo != 'F':
#         print('Sexo inválido!')
#         break
#     nomes.append(nome)
#     idades.append(idade)
#     sexos.append(sexo)
#
# for i, sexo in enumerate(sexos):
#     if sexo == 'M':
#         idade_homens.append(idades[i])
#         nome_homem.append(nomes[i])
#     else:
#         idade_mulheres.append(idades[i])
#
# for c, idade in enumerate(idade_mulheres):
#     if idade < 20:
#         mulher_menos_20 += 1
#
# media = sum(idades) / len(idades)
# velho = nome_homem[idade_homens.index(max(idade_homens))]
# if mulher_menos_20 > 1:
#     print(f'''
# A média de idade do grupo é {media} anos.
# O nome do homem mais velho é {velho}.
# Existem {mulher_menos_20} mulheres com menos de 20 anos nesse grupo.''')
#
# else:
#     print(f'''
# A média de idade do grupo é {media} anos.
# O nome do homem mais velho é {velho}.
# Existe {mulher_menos_20} mulher com menos de 20 anos nesse grupo.''')
