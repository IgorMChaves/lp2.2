print ("Informe três números diferentes para serem colocados em ordem crescente:")
x = 0
v = list(range(3))
while x < 3:
    v[x] = int(input('Informe um numero:'))
    x = x+1
    v.sort()
    print('Os números ordenados de forma crescente correspondem a: ',v)
