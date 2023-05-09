from datetime import date
print('-=' * 30)
print('Verifique sua situação em relação ao serviço militar:')
print('-=' * 30)
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
sexo = str(input('Digite [ F ] para feminino e [ M ] para masculino: ')).upper()
if sexo == 'F':
    print('Para mulheres o alistamento militar não é obrigatório. ')
elif sexo == 'M':
    if idade == 18:
        print(f'Quem nasceu em {nascimento} completa {idade} anos em 2023. Você precisa se alistar esse ano!')
    elif idade < 18:
        print(f'Quem nasceu em {nascimento} completa {idade} anos em 2023.\n'
              f'Ainda falta(m) {18 - idade} ano(s) para o alistamento.\n'
              f'Seu alistamento será em {ano_atual + (18 - idade)}.')
    elif idade > 18:
        print(f'Quem nasceu em {nascimento} completa {idade} anos em 2023.\n'
              f'Você já deveria ter se alistado há {idade - 18} ano(s).\n'
              f'Seu alistamento foi em {ano_atual - (idade - 18)}.')
else:
    print('Opção inválida. Tente novamente.')
