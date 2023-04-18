from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo para ver seu seno, cosseno e tangente: '))
print(f' Ângulo = {angulo}\n Seno = {sin(radians(angulo)):.2f}\n Cosseno = {cos(radians(angulo)):.2f}\n'
      f' Tangente = {tan(radians(angulo)):.2f} ')
