#   Minha Solução
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
    if sexo != 'F' and sexo != 'M':
        print('Opção Inválida. Tente novamente!')
print(f'Sexo {sexo} registrado com sucesso.')

#   Solução Professor:
# sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
# while sexo not in 'MF':
#     sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).upper().strip()[0]
# print(f'Sexo {sexo} registrado com sucesso.')

#   A solução do professor pega a primeira letra, então se digitarem 'Masculino' vai registrar o M.,
#   Porém, se digitar 'Música', ele entenderá Masculino também. Se digitar 'FM' ou 'MF' também vai aceitar.
