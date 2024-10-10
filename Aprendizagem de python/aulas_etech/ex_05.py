def contar(frase):
  espacos = 0
  vogais = 0
  vogais_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

  for letra in frase:
    if letra == ' ':
      espacos += 1
    elif letra in vogais_list:
      vogais += 1

  return espacos, vogais


frase = input("Digite uma frase qualquer: ")

num_espacos, num_vogais = contar(frase)
print(f'\nNúmero de espaços em branco: {num_espacos}')
print(f'\nNúmero de vogais: {num_vogais}\n')