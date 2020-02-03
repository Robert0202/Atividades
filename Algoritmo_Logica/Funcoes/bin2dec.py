def bin2dec(num):
    tamanho = len(num)
    potencia = 0
    result = 0
    for x in num:
      contvalor = (int(num[tamanho-1]))*(2**potencia)
      result+=contvalor
      potencia+=1
      tamanho-=1
    print(result)
    
num = input('Insira o valor Binario: ')
bin2dec(num)