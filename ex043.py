print('-=' * 20)
print('Calcule seu IMC agora mesmo!')
print('-=' * 20)
peso = float(input('Qual é o seu peso em KG? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} e você está na faixa "Magreza".')
elif 18.5 <= imc <= 24.9:
    print(f'Seu IMC é {imc:.1f} e você está na faixa "Normal".')
elif 25.0 <= imc <= 29.9:
    print(f'Seu IMC é {imc:.1f} e você está na faixa "Sobrepeso".')
elif 30.0 <= imc <= 39.9:
    print(f'Seu IMC é {imc:.1f} e você está na faixa "Obesidade".')
elif imc > 40:
    print(f'Seu IMC é {imc:.1f} e você está na faixa "Obesidade Grave".')
