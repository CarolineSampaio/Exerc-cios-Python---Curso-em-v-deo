#   Solução Otimizada
from random import randint
contador = 0
while True:
    print('=-' * 30)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. O total é {soma}, ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            contador += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENCEU!')
            contador += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar novamente...')
print('=-' * 30)
print(f'GAME OVER. Você venceu {contador} vezes.')

#   Primeira solução
# print('VAMOS JOGAR PAR OU IMPAR')
# jogador_ganha = True
# contador = 0
# while jogador_ganha:
#     print('=-' * 15)
#     jogador = int(input('Diga um valor: '))
#     escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
#     computador = randint(0, 10)
#     soma = jogador + computador
#     if soma % 2 == 0 and escolha == 'P':
#         print(f'Você jogou {jogador} e o computador {computador}. O total é {soma}, DEU PAR!')
#         print('Você VENCEU!')
#         print('Vamos jogar novamente...')
#         contador += 1
#     elif soma % 2 == 0 and escolha == 'I':
#         print(f'Você jogou {jogador} e o computador {computador}. O total é {soma}, DEU PAR!')
#         print('Você PERDEU!')
#         jogador_ganha = False
#     elif soma % 2 != 0 and escolha == 'P':
#         print(f'Você jogou {jogador} e o computador {computador}. O total é {soma}, DEU ÍMPAR!')
#         print('Você PERDEU!')
#         jogador_ganha = False
#     elif soma % 2 != 0 and escolha == 'I':
#         print(f'Você jogou {jogador} e o computador {computador}. O total é {soma}, DEU ÍMPAR!')
#         print('Você VENCEU!')
#         print('Vamos jogar novamente...')
#         contador += 1
#     else:
#         print('Opção inválida')
# print('=-' * 15)
# print(f'GAME OVER. Você venceu {contador} vezes.')
