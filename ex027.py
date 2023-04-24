nome = input('Qual é o seu nome completo?').strip()
div = nome.split()
print(f'Seu primeiro nome é {div[0]} e seu último nome é {div[-1]}')
