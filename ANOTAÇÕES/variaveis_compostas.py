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

    ### TUPLAS ### 
minha_tupla = ('minha_tupla: ',1,2,3,4,5,'ai',True,7.75)
print(minha_tupla)
print(minha_tupla[0])
print(minha_tupla[-1])
print(minha_tupla.count(3))
print(minha_tupla.index(7.75))
print(len(minha_tupla))

    ### DICIONÁRIOS ###
minha_dict = {'nome':'Joaquim','sobrenome':'Silva','idade':30}
print('dict:', minha_dict['idade'])
dicionario_vazio = {}
print(dicionario_vazio)
print(minha_dict.keys())
print(minha_dict.values())
print(minha_dict.items())
minha_dict['idade'] = 31  #forma para alterar um item do dict
print(minha_dict)
print(minha_dict.get('idade')) #forma mais eficientepara pegar um item do dict
minha_dict.update({'nome':'Joãozinho','sobrenome':'Macaco','idade':40})
print(minha_dict)