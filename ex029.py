vel = float(input('Qual é a velocidade atual do carro (km/h): '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'MULTADO. Você ultrapassou o limite de 80km/h permitido para a via.\n'
          f'O valor da multa é R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança.')
