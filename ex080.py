""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""
lista_num = []

for i in range(5):
    num = int(input(f'Digite um valor: '))
    if not lista_num or num > lista_num[-1]:
        lista_num.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista_num):
            if num <= lista_num[pos]:
                lista_num.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('=-' * 30)
print(f'Os valores digitados, em ordem crescente, foram {lista_num}')
