from time import sleep
print('-=' * 30)
print('Simule seu empréstimo bancário agora mesmo!')
print('-=' * 30)
valor_casa = float(input('Qual é o valor da casa que você deseja comprar?R$ '))
salario = float(input('Qual é o seu salário?R$ '))
tempo = int(input('Em quantos anos você deseja pagar? '))
parcela = valor_casa / (tempo * 12)
max_parcela = salario * 0.3
print(f'PROCESSANDO...')
sleep(2)
print(f'Para um empréstimo de R${valor_casa:.2f} em {tempo} anos, a parcela terá o valor de R${parcela:.2f}.')
if parcela <= max_parcela:
    print('Considerando sua renda, seu empréstimo pode ser concedido!')
else:
    print('Desculpe, infelizmente sua renda não é compatível para realizar esse empréstimo.')
