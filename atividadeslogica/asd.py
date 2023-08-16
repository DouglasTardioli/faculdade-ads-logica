print('Calculadora - Fornecimento de Energia!')
print()


while True:
    kwh = float(input('Insira a quantidade de kWh consumida:'))
    if kwh == 0:
        print('Não conseguimos calcular este valor, fechando programa...')
        break
    te = input('Insira o tipo de instalações para Residênciais (r), Indústriais (i) e Comércio (c):')
    if (te == 'r'):
        if (kwh <= 500 and kwh > 0):
            res = 0.40
        else:
            res = 0.65
    elif (te == 'i'):
        if (kwh <= 5000):
            res = 0.55
        else:
            res = 0.60
    elif (te == 'c'):
        if (kwh <= 100):
            res = 0.55
        else:
            res = 0.60
    else:
        print('fechando programa')
    print('O valor a ser pago é de R$ {:,.2f}'.format(kwh * res))