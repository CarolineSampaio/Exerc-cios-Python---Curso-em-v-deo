n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite um último número: '))
lista = (n1, n2, n3)
maior = max(lista)
menor = min(lista)
print(f'O menor valor digitado foi {menor}\n'
      f'O maior valor digitado foi {maior}')

# # Solução sugerida pelo professor:
# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# n3 = int(input('Terceiro valor: '))
# # Verificando menor:
# menor = n1
# if n2 < n1 and n2 < n3:
#     menor = n2
# if n3 < n1 and n3 < n2:
#     menor = n3
# # Verificando maior:
# maior = n1
# if n2 > n1 and n2 > n3:
#     maior = n2
# if n3 > n1 and n3 > n2:
#     maior = n3
# print(f'O menor valor digitado foi {menor}')
# print(f'O maior valor digitado foi {maior}')
