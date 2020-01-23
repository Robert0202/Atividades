import os
x = 0

clear = lambda: os.system('cls')

def dec2bin(number):
    return bin(number)

def bin2dec(number):
    return int(number, 2)

def dec2hex(number):
    return hex(number)

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

        elif int(x) == 2:
            number = input("Insira o numero binario: ")
            if number.isdecimal():
                binarynumbers = '01'
                count = 0
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
                print('Esse número não é um numero')
                str(input('Pressione qualquer tecla + Enter para continuar! : '))
                x = 0
                clear()
        
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



    