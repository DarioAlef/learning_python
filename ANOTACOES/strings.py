#em python tudo é objeto. Ao se criar uma variável com uma string,cria-se um objeto do tipo string
#Objetos possuem ATRIBUTOS (características) -> objeto.atributo()
#Objetos possuem MÉTODOS (ações que podem ser aplicadas)

#tamanho se uma string
a = "Dário Alef Barros lima\n\n"
tamanho = len(a)
print(tamanho)

#navegação pelo índice
print(a[0:2])

#-----------MÉTODOS-------
#alterando a caixa da string
print(a.lower())
print(a.upper())

#remover caracteres especiais
print(a.strip())

#converte a string em uma lista (array, podendo ser quebrada aonde quiser)
minha_string = "o rato roeu a roupa do rei de Roma" #(em roma não quebrou pois é r maiúsculo = case sensitive)
print(minha_string.split("r")) 

#buscar índice
print(minha_string.find("rei"))

#substituir partes de uma string
print(minha_string.replace("rei", "rainha"))

# FORMATED STRING: 
nome = 'Dário Alef'
peso = 80
print(f'\nOlá, meu nome é {nome} e eu peso {peso} quilos\n')

a = 50
b = 17
print(f'A soma de {a} + {b} é igual a {a + b}\n')

valor = 10/3
print(f'O valor é {valor}\n')
print(f'O valor é {valor:.2f}\n')