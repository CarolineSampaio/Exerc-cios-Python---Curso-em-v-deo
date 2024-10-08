""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta."""

expressao = input("Digite a expressão matemática: ")
pilha = []

for expr in expressao:
    if expr == '(':
        pilha.append('(')
    elif expr == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')
