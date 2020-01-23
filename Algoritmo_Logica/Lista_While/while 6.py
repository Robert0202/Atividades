media = 0
maiorn = 0
cont =0
soma = 0
numero = int(input(" infome um valor "))

if(numero > maiorn):
    maiorn = numero
    menorn = numero
    soma += numero
    cont += 1
continuar = str(input('Deseja continuar, sim ou não ? '))

while(continuar == 'sim' or continuar == 'Sim'):
    numero = int(input(" infome um valor "))
    if(numero < menorn):
        menorn = numero
        soma += numero
    elif(numero > maiorn):
        maiorn = numero
        soma += numero
    else:
       soma += numero
    cont += 1
    continuar = str(input('Deseja continuar, sim ou não ? '))
media = soma / cont

print(cont)
print('Media: {}'.format(media))
print('Menor Numero: {}'.format(menorn))
print('Maior Numero: {}'.format(maiorn))
