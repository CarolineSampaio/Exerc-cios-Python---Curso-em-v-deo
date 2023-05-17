#   Minha solução
print('=' * 30)
print('{:^30}'.format('LOJA BOM BARATO'))
print('=' * 30)
total_gasto = mais_mil = 0
produto_mais_barato = ''
preço_mais_barato = float('inf')
while True:
    produto = input('Nome do Produto: ')
    preço = float(input('Preço: R$ '))
    total_gasto += preço
    if preço > 1000:
        mais_mil += 1
    if preço < preço_mais_barato:
        produto_mais_barato = produto
        preço_mais_barato = preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'''O total da compra é de R$ {total_gasto:.2f}.
Temos {mais_mil} produtos custando mais de R$1000.00.
O produto mais barato foi {produto_mais_barato} que custa R$ {preço_mais_barato:.2f}.''')

#   Solução Professor:
# total = total_mil = menor = cont = 0
# barato = ''
# while True:
#     produto = str(input('Nome do Produto: '))
#     preço = float(input('Preço: R$ '))
#     cont += 1
#     total += preço
#     if preço > 1000:
#         total_mil += 1
#     if cont == 1 or preço < menor:
#         menor = preço
#         barato = produto
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print('{:-^30}'.format('FIM DO PROGRAMA'))
# print(f'''O total da compra é de R$ {total:.2f}.
# Temos {total_mil} produtos custando mais de R$1000.00.
# O produto mais barato foi {barato} que custa R$ {menor:.2f}.''')
