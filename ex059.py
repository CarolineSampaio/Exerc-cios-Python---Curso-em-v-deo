from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
menu = 0
while menu != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    menu: int = int(input('>>>> O que deseja fazer? '))

    if menu == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}.')
    elif menu == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}.')
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior valor é {maior}.')
    elif menu == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif 5 == menu:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('===' * 10)
    sleep(1)
print('Operação finalizada.')
