number = int(input('Digite um número para ver sua tabuada: '))
for multiple in range(1, 11):
    print(f'{number} x {multiple:2} = {number * multiple:2}')
