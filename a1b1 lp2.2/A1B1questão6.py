p = str(input('Informe uma palavra: '))
contrário = (p[::-1])
if p == contrário:
    print('Esta palavra é um palíndromo')
else:
    print('Esta palavra não é um palíndromo')
