num = int(input('Insira um número: '))
fat = 1
for j in range (num,1,-1):
    fat = fat*j
    print('O',num,'! é igual a:',fat)