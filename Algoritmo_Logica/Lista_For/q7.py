intervalo1 = intervalo2 = intervalo3 = intervalo4 = 0
for x in range (5) :
    numero =int(input(" informe seu numero "))
    if numero >=0 and numero <=25 :
     intervalo1 += 1
    elif (numero >= 26 and numero <=50):
        intervalo2 += 1
    elif (numero >= 51 and numero <= 75 ):
        intervalo3 += 1
    elif (numero >= 76 and numero <= 100 ):
        intervalo4 += 1
        print(intervalo1, intervalo2, intervalo3, intervalo4)

