# Solução quando precisa das variáveis para outra coisa:
# numero_int = int(input('Digite um número inteiro: '))
# sucessor = numero_int + 1
# antecessor = numero_int - 1
# print(f' O número escolhido: {numero_int}\n Seu sucessor é {sucessor} \n Seu antecessor é {antecessor}')

# Solução melhorada:
numero_int = int(input('Digite um número inteiro: '))
print(f' O número escolhido: {numero_int}\n Seu sucessor é {numero_int + 1} \n Seu antecessor é {numero_int - 1}')

