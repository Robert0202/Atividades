import random
x = int ( input(" informe o numero: "))
soma = 0
for y in range (1, x+1) :
    numero =random.randint(1,10 )
    soma += numero
    print(soma)
