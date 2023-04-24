nome = str(input('Qual é o seu nome completo? ')).strip()
dividir = (nome.split())
juntar = ''.join(dividir)
print(f'Analisando seu nome...\nSeu nome em  maiúsculas é {nome.upper()}\n'
      f'Seu nome em minúsculas é {nome.lower()}\n'
      f'Seu nome tem ao todo {len(juntar)} letras\n'
      f'Seu primeiro nome é {dividir [0]} e tem {len(dividir[0])} letras')

# Outra possibilidade para contar as letras sem o espaço é utilizar o count:
# cont = len(nome) - nome.count(' ')
# print(f'Seu nome completo tem {cont} letras')

# Outra possibilidade para descobrir o número de letras do primeiro nome, podemos usar o find, pois ele buscará o
# primeiro espaço e retorna o número da posição do caractere que será igual ao do primeiro nome.
# find = nome.find(' ')
# print( f'Seu primeiro tem {find} letras')
