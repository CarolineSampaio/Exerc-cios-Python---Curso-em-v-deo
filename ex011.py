largura = float(input('Qual é a largura da parede que você quer pintar? '))
altura = float(input('E qual é a altura? '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem {area}m² e para pinta-la você precisará de {tinta:.2f} litros de tinta')
