c = 0
while c != 4:
    x = int(input('Insira um número'))
    y = int(input('Insira um número'))
    con = int(input('''Insira um dos seguintes valores./n
        1 - Soma
        2 - Multiplicação
        3 - Informar novos números
        4 - Sair do Programa'''))
    if con == 1:
        print(f'A soma de {x} e {y} é: {x+y}')
    elif con == 2:
        print(f'A soma de {x} e {y} é: {x*y}')
    elif con == 3:
        c = 3
    elif con == 4:
        c = 4
print('Encerrado')
