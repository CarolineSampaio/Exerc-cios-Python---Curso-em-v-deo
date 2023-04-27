dist = float(input('Qual é a distância da viagem que você pretende fazer (km)? '))
if dist <= 200:
    preço = dist * 0.50
    print(f'Sua viagem custará R$ {preço:.2f}.')
else:
    preço = dist * 0.45
    print(f'Sua viagem custará R$ {preço:.2f}.')

# # if in line - simplificado
# dist = float(input('Qual é a distância da viagem que você pretende fazer (km)? '))
# preço = dist * 0.50 if dist <= 200 else dist * 0.45
# print(f"Sua viagem custará R$ {preço:.2f}.")
