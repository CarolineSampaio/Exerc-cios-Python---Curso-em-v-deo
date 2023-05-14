print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos números você quer ver? '))
t1 = 1
t2 = 1
t3 = 1
contador = 0
while contador < n:
    print(t1, end=' → ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    contador += 1
print('FIM')

# atribuição múltipla
# t1, t2 = t2, t1 + t2
