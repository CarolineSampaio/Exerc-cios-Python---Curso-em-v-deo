print('{:-^40}'.format('LOJA MULTI-COISAS'))
preço = float(input('Valor total da compra:R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
condição = int(input('Qual é a opção escolhida?  '))
if condição == 1:
    total = preço - (preço * 10 / 100)
elif condição == 2:
    total = preço - (preço * 5 / 100)
elif condição == 3:
    total = preço
    parcela = preço / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif condição == 4:
    total = preço + (preço * 20 / 100)
    tot_parc = int(input('Quantas parcelas? '))
    parcelas = total / tot_parc
    print(f'Sua compra será parcelada em {tot_parc}x de R${parcelas:.2f} COM JUROS. ')
else:
    total = preço
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente.')
print(f'Sua compra de R${preço:.2f}, vai custar R$ {total:.2f} no final.')
