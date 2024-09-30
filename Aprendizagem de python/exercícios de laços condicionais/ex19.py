altura = float(input("Digite a sua altura: "))
genero = str(input("Digite o seu gênero: "))
if genero == "homem":
    ph = (62.1 * altura) - 44.7
    print("Seu peso ideal é: ", ph)
else: 
    pm = (72.7 * altura) - 58
    print("Seu peso ideal é: ", pm)