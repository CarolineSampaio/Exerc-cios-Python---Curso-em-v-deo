from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print(f'PROCESSANDO...')
sleep(2)
print(f'O número que eu pensei foi {computador} e você digitou {jogador}.')
if jogador == computador:
    print('Parabéns você adivinhou o número!')
else:
    print('Infelizmente você não acertou o número :/.')

# 1 - computador escolhe número inteiro de 0 a 5
# 2 - usuário tenta adivinhar número
# 3 - se o usuário acertar == parabéns
# 4 - Se não, usuário perdeu.
