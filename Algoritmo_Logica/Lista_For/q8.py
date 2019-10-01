for x in range (5):
    altura = eval(input(" informe a altura "))
    if x==0 :
        maior = menor= altura
        if maior < altura :
            maior = altura
        elif menor > altura:
            menor = altura
print("maior:", maior )
print("menor:", menor )
