#   Minha solução inicial:
# for numero in range(1, 51):
#     if numero % 2 == 0:
#         print(numero)

#   Solução otimizada, diminuindo número de repetições do laço, e consequentemente, o esforço do processador:
for numero in range(2, 51, 2):
    print(numero, end=' ')
print('Acabou')
