for x in range (1, 101):
 soma = 0
 for y in range (1, x+1):
    if x % y ==0 :
      soma += y
      if soma == (x*2):
         print(x)
