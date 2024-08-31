""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem, de 0 a 20.
Seu Programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

continuar = True
while continuar:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')

    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
               'dezoito', 'dezenove', 'vinte')

    print(f'Você digitou o número {extenso[num]}.')
    resposta = input('Deseja continuar? Digite "s" para sim ou "n" para não:  ').strip().lower()

    if resposta != 's':
        continuar = False
