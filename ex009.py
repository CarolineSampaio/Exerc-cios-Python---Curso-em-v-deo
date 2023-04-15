num = int(input('Digite um número para ver sua tabuada: '))
print('_' * 12)
print(f' {num} x {1:2} = {num * 1}\n {num} x {2:2} = {num * 2}\n {num} x {3:2} = {num * 3}\n {num} x {4:2} = {num * 4}\n {num} x {5:2} = {num * 5}\n'
      f' {num} x {6:2} = {num * 6}\n {num} x {7:2} = {num * 7}\n {num} x {8:2} = {num * 8}\n {num} x {9:2} = {num * 9}\n {num} x 10 = {num * 10}')
print('_' * 12)

# Soluções mais avançadas encontradas:
# num = 1
# while num <= 10:
#     print(f' {num} x {num} = {num * num}')
#     num += 1


# print('\n'.join([f' {num} x {num} = {num * num}' for num in range(1, 10)]))
