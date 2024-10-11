dia = int(input("Digite um número de 1 a 7 respectivos aos dias da semana: "))
if dia <= 0 or dia > 7: 
    print("Esses valores não são válidos")
elif dia == 1:
    print("Domingo")
elif dia == 2:
    print("segunda-feira")
elif dia == 3:
    print("terça-feira")
elif dia == 4:
    print("quarta-feira")
elif dia == 5:
    print("quinta-feira")
elif dia == 6:
    print("sexta-feira")
elif dia == 7:
    print("sábado")
