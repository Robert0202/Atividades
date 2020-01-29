import os
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
valorEntrega = 1
valorCor = 1

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
                print('Valor Final:', valorfinal)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 2):
                valorfinal = (valorIx35 * valorEntrega) + ((valorIx35 * valorCor) - valorIx35) 
                print('Valor Final:', valorfinal)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 3):
                valorfinal = (valorAsx * valorEntrega) + ((valorAsx * valorCor) - valorAsx) 
                print('Valor Final:', valorfinal)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

            if(optioncar == 4):
                valorfinal = (valorSportage * valorEntrega) + ((valorSportage * valorCor) - valorSportage) 
                print('Valor Final:', valorfinal)
                str(input('Pressione qualquer tecla + Enter '))
                clear()

    #Carros Sedan
    
    #Carros Hatch

    #Carros Esportivos

