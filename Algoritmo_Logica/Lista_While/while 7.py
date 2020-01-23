c = 1
par = 0
impar = 0
while c != 0:
    x = int(input('Insira um número, para encerrar a execução insira 0.'))
    if x == 0:
        c -= 1
        par -= 1
    if x % 2 == 0:
        par +=1
    elif not x % 2 == 0:
        impar += 1
print(f'Foram digitados {par} números pares e {impar} números impares.')
