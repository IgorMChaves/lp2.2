try:
    x = int(input('Insira um número: '))
    y = int(input('Insira outro número: '))
    print(x, '/', y, '=', x / y)
except ValueError:
    print('Valores não validados. Tente números inteiros')
    x = int(input('Insira um número: '))
    y = int(input('Insira outro número: '))
    print(x, '/', y, '=', x / y)
except ZeroDivisionError:
    print ('Não foi possivel realizar a divisão por 0. Tente outro valor')
    x = int(input('Insira um número: '))
    y = int(input('Insira outro número: '))
    print(x, '/', y, '=', x / y)