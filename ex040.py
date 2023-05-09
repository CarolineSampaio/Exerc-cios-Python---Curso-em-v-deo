from time import sleep
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'PROCESSANDO...')
sleep(2)
if media < 5.0:
    print(f'Considerando as notas {nota1} e {nota2}, a média é {media:.1f}.\nO aluno está REPROVADO.')
elif 5 <= media <= 6.9:
    print(f'Considerando as notas {nota1} e {nota2}, a média é {media:.1f}.\nO aluno está de RECUPERAÇÃO.')
elif media >= 7:
    print(f'Considerando as notas {nota1} e {nota2}, a média é {media:.1f}.\nO aluno está APROVADO.')
