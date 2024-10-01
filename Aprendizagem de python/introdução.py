# -*- coding: utf-8 -*-    #serve para o python interpretar acentos em português

"""isso é um 
comentario"""

print(2+2)
print((2**3) % (5/2))#expoente

var1 = 1          #inteiro
var2 = 1.1        #float
var3 = "String"   #string
var4 = True       #booleana
var4 = False      #o 2° valor atribuído sobrepõe o primeiro valor

print(var1)
print(var2)
print(var3)
print(var4)

#---------ESTRUTURAS LÓGICAS--------------
x = 3
y = 2
z = 3

print(x == y and x == z)
print(x == y or x == z)

a = -2
b = -1

#---------ESTRUTURAS CONDICIONAIS-----------------
if b > a:
    if b > 0:
        print("b é amior que a\nb é positivo")
    else:
        print("b não é positivo")
else:
    print("b é menor que a")
    
#várias condições: elif -> irá excutar a primeira condição que encontrar
#permite inserir mais uma condição em um if
x2 = 1
y2 = 2

if x == y:
    print("números iguais")
elif x < y:
    print("y maior que x")
elif y > x:
    print("y maior que x")
else:
    print("numeros diferentes")
    
#-----------LAÇOS DE REPETIÇÃO:------------
x3 = 1

while x3 < 10:
    print(x3)
    x3 += 1 #mesma coisa que: x = x + 1
    
lista1 = [1,2,3,4,5]
lista2 = ["olá","mundo","!"]
lista3 = [0,"olá","biscoito","bolacha",9.99,True]

for i in lista3:
    print(i)  #range retorna uma lista
    
for i in range(20,30,2): #1° = início, 2° = fim, 3° = parâmetro de ação
    print(i)

#DISSECANDO UMA VARIÁVEL

a = input('Digite algo: ')
print('O tipo primitivo é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo?', a.islower())
print('Está capitalizada (maiúsculas e minúsculas) ? ', a.istitle())

# RAIZ QUADRADA: num **(1/2)