medida = float(input(' Digite um valor em metros: '))
# cm = medida * 100
# mm = medida * 1000
# print(f' A medida {medida}m corresponde a {cm}cm e {mm}mm')

# # Desafio extra
print(f' A medida {medida} m corresponde a:\n {medida / 1000} km\n {medida / 100} hm\n {medida / 10} dam\n'
      f' {medida*10} dm\n {medida*100} cm\n {medida*1000} mm')
