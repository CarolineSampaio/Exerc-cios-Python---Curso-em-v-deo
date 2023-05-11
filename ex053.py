frase = str(input('Digite uma frase: ')).upper().strip().split()
frase = ''.join(frase)
frase_contra = ''
for letra in frase:
    frase_contra = letra + frase_contra
print(f'O inverso de {frase} é {frase_contra}.')
if frase == frase_contra:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')

# Usando fatiamento de string
# if frase == frase[::-1]:
#     print("palíndromo")
