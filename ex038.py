n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
if n1 > n2:
    print(f'O primeiro valor digitado foi o {n1} e é maior do que {n2}.')
elif n2 > n1:
    print(f'O segundo valor digitado foi o {n2} e é maior do que o {n1}.')
else:
    print(f'Não existe valor maior, os dois são iguais.')
