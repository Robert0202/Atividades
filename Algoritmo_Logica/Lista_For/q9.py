positivo = negativos = soma = 0
for x in range(20):
        n = int(input(" infome os numeros "))
        soma +=n
        if n > 0 :
         positivo += 1
        elif n<0 :
            negativos += n
soma = soma/ 20
print(" media aritmetica ", soma)
print(" quantidade de valores positivo ", positivo)
print(" somatorio de valores negativos ", negativos)
