import os
x = 0
#@clear - Variavel para limpar o console
clear = lambda: os.system('cls')

#Funções

#Recebe um valor decimal e retorna em binario
def dec2bin(number):
    return bin(number)

#Recebe um valor binario e retorna em decimal
def bin2dec(number):
    return int(number, 2)

#Recebe um valor decimal e retorna em hexadecimal
def dec2hex(number):
    return hex(number)

#Recebe um valor hexadecimal e retorna em decimal
def hex2dec(number):
    return int(number, 16)

#Recebe um valor binario e retorna em octal
def bin2oct(number):
    return oct(number)

#Recebe um valor octal e retorna em binario
def oct2bin(number):
    return bin(number)

#Recebe um valor binario, transforma para decimal e retorna em hexadecimal
def bin2hex(number):
    decimalnumber = bin2dec(number) 
    hexanumber = dec2hex(decimalnumber)
    return hexanumber

#Recebe um valor hexadecimal, transforma para decimal e retorna em binario
def hex2bin(number):
    decimalnumber = hex2dec(number)
    binarynumber = dec2bin(int(decimalnumber))
    return binarynumber
#Fim das funções


#Start do programa
while(int(x) != 9):
    print("[1] Converter um número decimal para binário")
    print("[2] Converter um número binário para decimal")
    print("[3] Converter um número decimal para hexadecimal")
    print("[4] Converter um número hexadecimal para decimal")
    print("[5] Converter um número binário para octal")
    print("[6] Converter um número octal para binário")
    print("[7] Converter um número binário para hexadecimal")
    print("[8] Converter um número hexadecimal para binário")
    print("[9] Encerrar o programa")

    x = input("Escolha uma opção: ")
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    if x.isdecimal():

        #Se a opção for 1 entra nessa condição
        #@is.decimal - faz o check se o numero é do tipo decimal
        #@dec2bin - chama a função responsavel por converter o número
        if int(x) == 1:
            number = input("Insira o numero decimal: ")
            if number.isdecimal():
                binarynumber = dec2bin(int(number))
                print("Em Binario: ", binarynumber)
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()
            else:
                print('Esse número não é um decimal')
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()

        #Se a opção for 2 entra nessa condição
        #@is.decimal - faz o check se o numero é do tipo decimal
        #@bin2dec - chama a função responsavel por converter o número
        elif int(x) == 2:
            number = input("Insira o numero binario: ")
            if number.isdecimal():
                binarynumbers = '01'
                count = 0
                # FOR para saber se todos os numeros são 0 ou 1
                for char in number:
                    if char not in binarynumbers:
                        count = 1
                        break
                    else:
                        pass
                if count:
                    print('Você inseriu um binario invalido ')
                    str(input('Pressione qualquer tecla + Enter para continuar! : '))
                    x = 0
                    clear()
                else:
                    decimalnumber = bin2dec(number) 
                    print("Em Decimal: ", decimalnumber)
                    str(input('Pressione qualquer tecla + Enter para continuar! : '))
                    clear()
                    x = 0
            else:
                print('Esse valor não é um numero')
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()

        #Se a opção for 3 entra nessa condição
        #@is.decimal - faz o check se o numero é do tipo decimal
        #@dec2hex - chama a função responsavel por converter o número
        elif int(x) == 3:
            number = input("Insira o numero decimal: ")
            if number.isdecimal():
                hexnumber = dec2hex(int(number)) 
                print("Em Hexadecimal: ", hexnumber)
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()
            else:
                print('Esse número não é um decimal')
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()

        #Se a opção for 4 entra nessa condição
        #@hex2dec - chama a função responsavel por converter o número
        elif int(x) == 4:
            number = input("Insira o numero hexadecimal: ") 
            decimalnumber = hex2dec(number)
            print("Em decimal: ", decimalnumber)
            str(input('Pressione qualquer tecla + Enter para continuar! : '))
            x = 0
            clear()

        #Se a opção for 5 entra nessa condição
        #@is.decimal - faz o check se o numero é do tipo decimal
        #@bin2oct - chama a função responsavel por converter o número
        elif int(x) == 5:
            number = input("Insira o numero binario: ")
            if number.isdecimal():
                binarynumbers = '01'
                count = 0
                # FOR para saber se todos os numeros são 0 ou 1
                for char in number:
                    if char not in binarynumbers:
                        count = 1
                        break
                    else:
                        pass
                if count:
                    print('Você inseriu um binario invalido ')
                    str(input('Pressione qualquer tecla + Enter para continuar! : '))
                    x = 0
                    clear()
                else:
                    decimal = bin2dec(number)
                    octalnumber = bin2oct(int(decimal)) 
                    print("Em Octal: ", octalnumber)
                    str(input('Pressione qualquer tecla + Enter para continuar! : '))
                    clear()
                    x = 0
            else:
                print('Esse valor não é um numero')
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()

        #Se a opção for 6 entra nessa condição
        #@is.decimal - faz o check se o numero é do tipo decimal
        #@oct2bin - chama a função responsavel por converter o número
        elif int(x) == 6:
            number = input("Insira o numero octal: ")
            if number.isdecimal():
                decimalnumber = int(number, 8)
                binarynumber = oct2bin(int(decimalnumber))
                print("Em Binario: ", binarynumber)
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                clear()
                x = 0
            else:
                print('Esse valor não é um numero valido')
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()

        #Se a opção for 7 entra nessa condição
        #@is.decimal - faz o check se o número é do tipo decimal
        #@bin2hex - chama a função responsavel por converter o número
        elif int(x) == 7:
            number = input("Insira o numero binario: ")
            if number.isdecimal():
                binarynumbers = '01'
                count = 0
                # FOR para saber se todos os numeros são 0 ou 1
                for char in number:
                    if char not in binarynumbers:
                        count = 1
                        break
                    else:
                        pass
                if count:
                    print('Você inseriu um binario invalido ')
                    str(input('Pressione qualquer tecla + Enter para continuar! : '))
                    x = 0
                    clear()
                else:
                    hexanumber = bin2hex(number)
                    print("Em Hexadecimal: ", hexanumber)
                    str(input('Pressione qualquer tecla + Enter para continuar! : '))
                    clear()
                    x = 0
            else:
                print('Esse valor não é um numero')
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()

        #Se a opção for 8 entra nessa condição
        #@hex2bin - chama a função responsavel por converter o número
        elif int(x) == 8:
            number = input("Insira o numero Hexadecimal: ")
            binarynumber = hex2bin(number)
            print("Em Binario: ", binarynumber)
            str(input('Pressione qualquer tecla + Enter para continuar! : '))
            clear()
            x = 0

        #Caso o usuario insira uma opção que não exista irá cair nessa condição
        elif int(x) not in options:
            print('Opção inexistente!')
            str(input('Pressione qualquer tecla + Enter para continuar! : '))
            x = 0
            clear()

    else:
        print('Você inseriu um valor invalido')
        str(input('Pressione qualquer tecla + Enter para continuar! : '))
        x = 0
        clear()



    