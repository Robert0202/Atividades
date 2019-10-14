soma = 0
cont = 0
numero = int(input(" informe um numero: "))
while(numero >= 0):
    soma += numero
    cont += 1
    numero = int(input(" informe um numero: "))

print('A soma dos numeros: {}'.format(soma))
print('total de numeros somados: {}'.format(cont))
