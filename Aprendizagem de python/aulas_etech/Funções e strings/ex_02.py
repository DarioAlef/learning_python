def inverter_num(num):
  num_str = str(num)

  num_invertido_str = num_str[::-1]

  num_invertido = int(num_invertido_str)

  return num_invertido


num = int(input('Digite um número: '))
print(f'\nO número invertido é: {inverter_num(num)}')