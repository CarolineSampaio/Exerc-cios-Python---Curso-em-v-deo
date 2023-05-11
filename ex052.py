num = int(input('Digite um número: '))
contador = 0
for i in range(1, num+1):
    if num % i == 0:
        contador += 1
    if contador == 3:
        break
if contador == 2:
    print(f'O número {num} é PRIMO.')
else:
    print(f'O número {num} NÃO é primo.')
