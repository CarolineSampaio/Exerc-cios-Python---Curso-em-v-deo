from datetime import date
print('Bem vindo a página da Confederação Nacional de Natação!\n'
      'Descubra sua categoria abaixo:')
ano_atual = ano = date.today().year
nascimento = int(input('Qual é o ano do seu nascimento(AAAA)? '))
idade = ano_atual - nascimento
if idade <= 9:
      print(f'O atleta tem {idade} anos.\nClassificação: MIRIM')
elif idade <= 14:
      print(f'O atleta tem {idade} anos.\nClassificação: INFANTIL')
elif idade <= 19:
      print(f'O atleta tem {idade} anos.\nClassificação: JUNIOR')
elif idade <= 25:
      print(f'O atleta tem {idade} anos.\nClassificação: SÊNIOR')
else:
      print(f'O atleta tem {idade} anos.\nClassificação: MASTER')
