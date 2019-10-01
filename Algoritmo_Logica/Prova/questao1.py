
x = int(input("Informe o primeiro numero"))
y = int(input("Informe o segundo numero"))

if x < y :
    for z in range (x, y+1, 1) :
        print(z)
elif x > y :
    for z in range (x, y-1, -1) :
        print(z)