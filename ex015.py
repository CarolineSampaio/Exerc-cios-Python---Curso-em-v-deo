dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
aluguel = (dias * 60) + (km * 0.15)
print(f'O valor total do seu aluguel é R${aluguel:.2f}.')
