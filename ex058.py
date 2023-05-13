from random import randint
computador = randint(0, 10)
print('-=-' * 22)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 22)
jogador = -1
tentativas = 0
while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez')

print('-=-' * 22)
print(f'Parabéns você adivinhou o número, você precisou de {tentativas} tentativas.')

#   Solução professor - != Usou booleano no while;

# from random import randint
# computador = randint(0, 10)
# print('-=-' * 22)
# print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
# print('-=-' * 22)
# acertou = False
# tentativas = 0
# while not acertou:
#     jogador = int(input('Qual é o seu palpite? '))
#     tentativas += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... Tente mais uma vez.')
#         elif jogador > computador:
#             print('Menos... Tente mais uma vez')
