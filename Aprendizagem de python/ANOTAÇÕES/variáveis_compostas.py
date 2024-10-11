sequencia = ['maçã','banana','abacaxi','laranja','manga']

for indice in enumerate(sequencia, start=1):
    print(indice)
#sequencia == o que será enumerado
#start == onde irá iniciar o contador

    ### LISTAS ### 
num = []       
for i in range(10):
    num.append(i) 
print(list(num))

lista = "Python"
print(list(lista))

lista_range = list(range(10))
print(lista_range)
print(lista[-1])

ultimo = lista.pop()
print(ultimo)