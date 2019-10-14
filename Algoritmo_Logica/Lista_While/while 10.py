print(f'o maior peso entremaior = 0')
con1 = 1
con2 = 0
c = 1
media1 = 0
mediafin = 0
media2 = 0
while c != 0:
    peso = float(input('Qual o peso da pessoa?'))
    idade = int(input('e a Idade?'))
    c = int(input('Deseja continuar a inserir informações ? 1 para sim 0 Para não.'))
    if idade < 45:
        con1 += 1
    if idade >=60 and idade <= 75:
        media1 += peso
        media2 += 1
        con2 += 1
    if peso > maior and idade < 12:
        maior = peso
if con2 >= 1:
    mediafin = media1 / media2
print(f'Tem {con1} Pessoas com menos de 45 anos.')
print(f'a media do peso das pessoas entre 60 e 75 anos é {mediafin}')
