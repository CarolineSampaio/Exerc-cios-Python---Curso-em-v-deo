valor_produto = float(input('Qual é o valor do produto? R$ '))
desconto = (valor_produto * 5) / 100
valor_final = valor_produto - desconto
print(f'O produto que custava R${valor_produto:.2f}, na promoção com desconto de 5% vai custar R${valor_final:.2f}')
