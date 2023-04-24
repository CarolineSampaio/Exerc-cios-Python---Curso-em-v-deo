cidade = input('Em que cidade você nasceu: ').strip()
dividir = cidade.upper().split()
verif = 'SANTO' in dividir[0]
print(f'O nome da cidade que você nasceu é {cidade}'
      f'e nos verificamos se ela começa com SANTO e encontramos a afirmação: {verif}')
