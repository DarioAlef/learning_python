def nome_escada(nome):
  for i in range(len(nome)):
    print(nome[:i+1])
#':i' começando em i e adicionando 1


nome = input("Digite seu nome: ")
nome_escada(nome)