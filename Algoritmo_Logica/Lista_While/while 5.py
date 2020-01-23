import random
cont = 0
numero = random.randint(1, 10)
while(numero != 10):
    cont += 1
    numero = random.randint(1, 10)
print('Foram gerados {} numeros para obter o numero 10'.format(cont))
