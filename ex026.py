frase = input('Digite uma frase: ').upper().strip()
quantidade = frase.count('A')
primeiro_a = frase.find('A') + 1
ultimo_a = frase.rfind('A') + 1
print(f'A letra A aparece {quantidade} vezes na frase.\n'
      f'A primeira letra A apareceu na posição {primeiro_a}.\n'
      f'A última letra A apareceu na posição {ultimo_a}.')
