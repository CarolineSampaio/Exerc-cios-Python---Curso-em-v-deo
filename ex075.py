""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
a)Quantas vezes apareceu o número 9, b)Em que posição foi digitado o primeiro valor 3, c)Quais foram os números pares."""

num = (int(input('Digite um número entre 0 e 10: ')),
       int(input('Digite mais um número entre 0 e 10: ')),
       int(input('Digite outro número entre 0 e 10: ')),
       int(input('Digite o último número entre 0 e 10: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 está na {num.index(3) + 1}° posição.')
else:
    print(f'O número 3 não foi digitado em nenhuma posição.')

pares = ()
for n in num:
    if n % 2 == 0:
        pares += (n,)
print(f'Os números pares digitados foram {pares}.')
