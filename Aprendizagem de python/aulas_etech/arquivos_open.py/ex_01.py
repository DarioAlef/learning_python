#python oferece várias maneiras para se ler e trabalhar com arquivos

#Lendo vários arquivos de uma vez:
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)