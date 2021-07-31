numero = int(input('Insira um numero: '))
vetor = []
j = 1
while j != numero:
    cont = 0
for i in range(1, j+1):
    if (j % i == 0)and(j!=2):
        cont = cont + 1
if cont==2:
    vetor.append(j)
    j = j + 1
    print('Os números primos encontrados entre 1 e ',numero,'equivalem a:',vetor)