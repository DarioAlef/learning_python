# Q.09 - peça e calcule o fatorial de um número (produto dele pelos seus antecessores maiores que 0)

numero = int(input("\nDigite um número inteiro positivo: "))

fatorial = 1
if numero < 0:
  print("\nO fatorial não está definido para números negativos.\n")

else:
  for i in range(1, numero + 1):
    fatorial *= i
# 4: --> fatorial = 1 * i  -->  
#        fatorial = 1 * 1  -->  fatorial = 1
#        fatorial = 1 * 2  -->  fatorial = 2
#        fatorial = 2 * 3  -->  fatorial = 6
#        fatorial = 6 * 4  -->  fatorial = 24

print(f"\nO fatorial de {numero} é {fatorial}\n")