peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em cm: "))
idade = int(input("Digite a sua idade: "))
genero = str(input("homem ou mulher? "))

tmbH = 88.362 + (13.397*peso) + (4.799*altura) - (5.677*idade)
tmbM = (10*peso) + (6.25*altura) - (5*idade) - 161

if genero == "homem":
    print("Sua Tx. metabólica basal é: ", tmbH)
else:
    print("Sua Tx. metabólica basal é: ", tmbM)