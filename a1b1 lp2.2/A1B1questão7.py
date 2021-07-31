print('Informe números para que se calcule a média')
laço = int(input('Informe um número: '))
n=0
s = 0
while laço != 0:
    s = s + laço
    laço = int(input('Informe um número: '))
    n=n+1
    print('A média dos números equivale a: ', s/n)