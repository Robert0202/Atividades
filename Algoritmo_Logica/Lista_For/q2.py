numero = int(input(" infome o numero "))
soma = 0
for x in range (1, numero+1) :
    if numero % x == 0 :
        soma += 1

if soma >0 and soma <= 2:
    print(" numero é primo ")
else :
    print(" numero nao é primo ")
