import os
import locale
#Atribuindo a variavel 'clear' a função de limpar o console
clear = lambda: os.system('cls')
#valores dos carros
x = 0
valorDuster = 75000
valorIx35 = 90000
valorAsx = 110000
valorSportage = 125000
valorKA = 58000
valorClassic = 30000
valorLogan = 50000
valorVoyage = 43000
valorOnix = 40000
valorHb20 = 39000
valorKahat = 37000
valorUno = 1000000
valorJetta = 175000
valorA1 = 200000
valorCooper = 120000
valorS60 = 245000

#Inicio
while(x != 2):
    print('Você deseja comprar qual tipo de veiculo ?')
    print('[1] SUV')
    print('[2] Sedan')
    print('[3] Hatch')
    print('[4] Esportivo')
    print('[5] Sair')
    option = int(input('Visualizar: '))
    clear()
    valorEntrega = 1
    valorCor = 1

    if(option == 5):
        exit()

    #Carros SUV
    if(option == 1):
        print('[1] Renault Duster - R$75.000,00')
        print('[2] Hyundai ix35 - R$90.000,00')
        print('[3] Mitsubish ASX - R$110.000,00')
        print('[4] KIA Sportage - R$125.000,00')
        print('[5] Voltar')
        optioncar = int(input('Desejo: '))

        if(optioncar != 5):
            print('Você vai querer serviço de entrega para o veiculo ?')
            print('[1] Sim ')
            print('[2] Não ')
            optionentrega = int(input(': '))
            if(optionentrega == 1):
                valorEntrega = 1.02

            print('Deseja comprar com cores exclusivas ou padrão ?')
            print('[1] Exclusiva')
            print('[2] Padrão')
            optioncor = int(input(': '))
            if(optioncor == 1):
                valorCor = 1.02

            if(optioncar == 1):
                valorfinal = (valorDuster * valorEntrega) + ((valorDuster * valorCor) - valorDuster) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 2):
                valorfinal = (valorIx35 * valorEntrega) + ((valorIx35 * valorCor) - valorIx35) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 3):
                valorfinal = (valorAsx * valorEntrega) + ((valorAsx * valorCor) - valorAsx) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 4):
                valorfinal = (valorSportage * valorEntrega) + ((valorSportage * valorCor) - valorSportage) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

    #Carros Sedan
    if(option == 2):
        print('[1] Ford KA Sedan - R$58.000,00')
        print('[2] Chevrolet Classic - R$30.000,00')
        print('[3] Renault Logan - R$50.000,00')
        print('[4] Volkswagem Voyage - R$43.000,00')
        print('[5] Voltar')
        optioncar = int(input('Desejo: '))

        if(optioncar != 5):
            print('Você vai querer serviço de entrega para o veiculo ?')
            print('[1] Sim ')
            print('[2] Não ')
            optionentrega = int(input(': '))
            if(optionentrega == 1):
                valorEntrega = 1.02

            print('Deseja comprar com cores exclusivas ou padrão ?')
            print('[1] Exclusiva')
            print('[2] Padrão')
            optioncor = int(input(': '))
            if(optioncor == 1):
                valorCor = 1.02

            if(optioncar == 1):
                valorfinal = (valorKA * valorEntrega) + ((valorKA * valorCor) - valorKA) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 2):
                valorfinal = (valorClassic * valorEntrega) + ((valorClassic * valorCor) - valorClassic) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 3):
                valorfinal = (valorLogan * valorEntrega) + ((valorLogan * valorCor) - valorLogan) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 4):
                valorfinal = (valorVoyage * valorEntrega) + ((valorVoyage * valorCor) - valorVoyage) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

    #Carros Hatch
    if(option == 3):
        print('[1] Chevrolet Onix - R$40.000,00')
        print('[2] Hyundai HB20 - R$39.000,00')
        print('[3] Ford Ka Hatch - R$37.000,00')
        print('[4] Fiat Uno - R$1.000.000,00')
        print('[5] Voltar')
        optioncar = int(input('Desejo: '))

        if(optioncar != 5):
            print('Você vai querer serviço de entrega para o veiculo ?')
            print('[1] Sim ')
            print('[2] Não ')
            optionentrega = int(input(': '))
            if(optionentrega == 1):
                valorEntrega = 1.02

            print('Deseja comprar com cores exclusivas ou padrão ?')
            print('[1] Exclusiva')
            print('[2] Padrão')
            optioncor = int(input(': '))
            if(optioncor == 1):
                valorCor = 1.02

            if(optioncar == 1):
                valorfinal = (valorOnix * valorEntrega) + ((valorOnix * valorCor) - valorOnix) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 2):
                valorfinal = (valorHb20 * valorEntrega) + ((valorHb20 * valorCor) - valorHb20) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 3):
                valorfinal = (valorKahat * valorEntrega) + ((valorKahat * valorCor) - valorKahat) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 4):
                valorfinal = (valorUno * valorEntrega) + ((valorUno * valorCor) - valorUno) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

    #Carros Esportivos
    if(option == 4):
        print('[1] Volkswagem Jetta Highline - R$175.000,00')
        print('[2] Audi A1Sportback - R$200.000,00')
        print('[3] Mini Cooper - R$120.000,00')
        print('[4] Volvo S60 - R$245.000,00')
        print('[5] Voltar')
        optioncar = int(input('Desejo: '))

        if(optioncar != 5):
            print('Você vai querer serviço de entrega para o veiculo ?')
            print('[1] Sim ')
            print('[2] Não ')
            optionentrega = int(input(': '))
            if(optionentrega == 1):
                valorEntrega = 1.02

            print('Deseja comprar com cores exclusivas ou padrão ?')
            print('[1] Exclusiva')
            print('[2] Padrão')
            optioncor = int(input(': '))
            if(optioncor == 1):
                valorCor = 1.02

            if(optioncar == 1):
                valorfinal = (valorJetta * valorEntrega) + ((valorJetta * valorCor) - valorJetta) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 2):
                valorfinal = (valorA1 * valorEntrega) + ((valorA1 * valorCor) - valorA1) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 3):
                valorfinal = (valorCooper * valorEntrega) + ((valorCooper * valorCor) - valorCooper) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 4):
                valorfinal = (valorS60 * valorEntrega) + ((valorS60 * valorCor) - valorS60) 
                locale.setlocale(locale.LC_ALL, '')
                valor = locale.currency(valorfinal, grouping=True)
                print('Valor Final:', valor)
                str(input('Pressione qualquer tecla + Enter '))
                clear()
