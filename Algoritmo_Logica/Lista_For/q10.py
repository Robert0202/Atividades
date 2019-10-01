media = 0
for x in range (1, 31):
    n = int(input(" informe a nota final: "))
    media += n
    if x == 0 :
        maior = menor = n
    else:
        if maior <n:
            maior = n
        elif menor > n:
            menor = n
media = media / 30
print(" media da turma ", media)
print(" maior nota ", maior)
print(" menor nota ", menor)
