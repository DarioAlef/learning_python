#1

gasolina = 2.25
distancia = 1000

veiculos = []
km_por_litro = []

print('\nInsira os dados abaixo para saber qual carro é mais econômico.\n')
for i in range(5):
    print(f'Veículo {i + 1}')
    veiculo = input('modelo: ')
    consumo = float(input('Km/L: '))

    veiculos.append(veiculo)
    km_por_litro.append(consumo)

for i in range(5):
    litros_consumidos = distancia / km_por_litro[i]
    custo = litros_consumidos * gasolina
    print(f'{i + 1} - {veiculos[i]} - {km_por_litro[i]:.1f} Km/L - {litros_consumidos:.1f} litros - R$ {custo:.2f}')

melhor_consumo = max(km_por_litro)
indice_melhor_consumo = km_por_litro.index(melhor_consumo)

print(f'\nO mais econômico é o {veiculos[indice_melhor_consumo]}')

#2
print('\nDigite abaixo o atleta e os seus saltos:\n')

while True:
    atleta = input("Atleta: ")

    saltos = []

    for i in range(5):
        salto = float(input(f"{i + 1}º Salto: "))
        saltos.append(salto)

    media_saltos = sum(saltos) / len(saltos)

    print(f"Atleta: {atleta}")

    print("Saltos: ", " - ".join(f"{salto:.1f}" for salto in saltos))

    print(f"Média dos saltos: {media_saltos:.1f} m\n")

#3

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
respostas_sim = 0

for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    if resposta == "sim":
        respostas_sim += 1

if respostas_sim == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_sim <= 4:
    classificacao = "Cúmplice"
elif respostas_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("\nClassificação:", classificacao)