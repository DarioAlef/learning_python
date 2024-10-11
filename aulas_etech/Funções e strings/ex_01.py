import random

def embaralhar_string(txt):
  list_txt = list(txt)

  random.shuffle(list_txt)

  txt_embaralhado = ''.join(list_txt)

  return txt_embaralhado


txt = str(input('Digite uma palavra: '))
palavra_embaralhada = embaralhar_string(txt)
print(f'\n{palavra_embaralhada.lower()}\n')