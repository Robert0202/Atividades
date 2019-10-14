numero = eval(input(" informe o primeiro numero "))
numero2 = eval(input(" informe o segundo numero "))
while numero>numero2 or numero<numero2 :
    if numero>numero2 :
        print(numero," é maior que ",numero2)
    elif numero2>numero :
        print(numero2," é maior que ",numero)
    numero = eval(input(" informe o primeiro numero "))
    numero2 = eval(input(" informe o segundo numero "))
print(" os dois numeros são equivalentes, OK ")



