#Q.5 -  Dado uma string com uma frase informada pelo usuário conte
#quantos espacos em branco existem e vogais existem na frase.

def contar(frase):
    espacos = 0
    vogais = 0
    for i in range(len(frase)):
        if frase[i] == ' ':
            espacos += 1
        elif frase[i] in 'aeiouAEIOU':
            vogais += 1

    return espacos, vogais


frase = str(input("\nDigite uma frase qualquer: "))
print(f'\nEspacos em branco: {contar(frase)[0]}')
print(f'\nVogais: {contar(frase)[1]}\n')