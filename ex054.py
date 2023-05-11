from datetime import date
menores = 0
maiores = 0
MAIOR_IDADE = 21

for pessoa in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu (AAAA): '))
    idade = date.today().year - nascimento
    if idade >= MAIOR_IDADE:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade\n'
      f'E também tivemos {menores} pessoas menores de idade')
