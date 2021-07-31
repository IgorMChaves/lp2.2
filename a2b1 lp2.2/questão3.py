def somaNum(a, b):
    if (a + b) > 1000:
        raise OverflowError
    else: 
        return a + b
try:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('O resultado da soma dos valores equivale a ', somaNum(v1, v2))
except ValueError:
    print('Valores não validados. Tente números inteiros')
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('O resultado da soma dos valores equivale a ', somaNum(v1, v2))
except OverflowError:
    print('Dados inesperados. Tente números cujo resultado da soma equivalha a um valor menor que 1000')
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('O resultado da soma dos valores equivale a ', somaNum(v1, v2))