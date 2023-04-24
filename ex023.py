n1 = input('Digite um número de 0 a 9999: ')
n2 = '000' + n1
print(f'unidade: {n2[-1]} \ndezena: {n2[-2]} \ncentena: {n2[-3]} \nmilhar: {n2[-4]}')

# Possibilidade de utilizar a matematica dividindo e depois pegando o resto da divisão.