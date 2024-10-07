#Q.13 - Use um laço para multiplicar números começando por 1 até que o produto seja maior que 1000

mult = 1

for i in range(1,1000):
    mult = mult * i

    if mult < 1001:
        print(mult)
        break