print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('ISÓSCELES.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO.')
else:
    print('Os segmentos acima não podem formar triângulo.')
