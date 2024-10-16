#Q.4 - Faça um programa para mostrar o nome em formato de escada

def nome_escada(nome):
    for i in range(len(nome)):
        print(nome[:i+1]) #range(len) para pecorrer toda a string
#imprime do começo da string, indicada por : até 'i, somando 1

nome = input("Digite seu nome: ")
nome_escada(nome)