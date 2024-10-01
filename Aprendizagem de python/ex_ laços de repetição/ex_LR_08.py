# Q.08 - Multiplique todos os números ímpares de 1 a 50
mult = 1
for i in range(1,50):
    if i % 2 != 0:
        mult = mult*i
print(f'A multiplicação de todos os números ímpares de 1 a 50 é: {mult}')

#-------------------------------------

mult_w = 1
j = 1
while j < 50:
    j+=1
    if j % 2 != 0:
        mult_w = mult_w * j
print(f'\nA multiplicação de todos os números ímpares de 1 a 50 é: {mult_w}')