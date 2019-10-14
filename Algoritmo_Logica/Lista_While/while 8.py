from random import randint
x = 0
cont = 0
y = 1
while x != y:
    x = randint(1,10)
    y = int(input('Qual o número aleatorio entre 1 e 10 que foi gerado?'))
    if x != y:

        print('Errado.')
    cont +=1
print(f'Acertou com {cont} tentativas.')
