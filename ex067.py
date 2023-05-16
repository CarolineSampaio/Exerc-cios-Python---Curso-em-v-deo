while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    print('_' * 40)
    if numero < 0:
        break
    for multiplo in range(1, 11):
        print(f'{numero} x {multiplo:2} = {numero * multiplo:2}')
    print('_' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
