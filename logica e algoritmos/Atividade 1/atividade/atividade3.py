print('Bem-vindo ao banho e tosa do Douglas Peixoto Tardioli')

preso = 0
multiplicador = 0

def pesoCachorro():
  
  while True:
          try:
            peso = int(input('Qual o peso do cachorro (kg): '))
            if peso < 3:
                preso = 40
                return preso
            elif peso >= 3 and peso < 10:
                preso = 50
                return preso
            elif peso >= 10 and peso < 30:
                preso = 60
                return preso
            if peso >= 30 and peso < 50:
                preso = 70
                return preso
            else:
                print('Não aceitamos cachorros tão grandes.')
          except ValueError:
              print('Você digitou um valor não numerico \n' +
                    'Por favor, entre com o peso do cachorro novamente')
              

def peloCachorro():
  while True:
      pelo_cachorro = input('Qual o Pelo do cachorro \n' + 
                            'c - Pelo Curto\n' +
                            'm = Pelo Médio\n' +
                            'l = Pelo Longo\n' +
                            ': ')
      pelo_cachorro = pelo_cachorro.lower()
      if pelo_cachorro == 'c':
          multiplicador = 1
          return multiplicador
      elif pelo_cachorro == 'm':
          multiplicador = 1.5
          return multiplicador
      elif pelo_cachorro == 'l':
          multiplicador = 2
          return multiplicador
      else:
          print('Digite uma das opções acima.')

def servicoExtra():
    accum = 0
    while True:
      extra = input('Deseja adicionar mais algum serviço: \n' + 
                            '0 - Não, desejo finalizar.\n' +
                            '1 - Cortes de unhas - R$10,00\n' +
                            '2 - Escovar Dentes - R$12,00\n' +
                            '3 - Limpeza de orelhas - R$15,00\n' +
                            ': ')
      if extra == '0':
          return accum
      elif extra == '1':
          accum += 10
          continue
      elif extra == '2':
          accum += 12
          continue
      elif extra == '3':
          accum += 15
          continue
      else:
          print('Digite uma das opções acima.')


peso_cachorro =  pesoCachorro()
pelo_cachorro =  peloCachorro()
servico_extra = servicoExtra()


total = (peso_cachorro * pelo_cachorro) + servico_extra
print(f'Total a pagar: R${total:.2f} (peso: R${peso_cachorro:.2f} * pelo: R${pelo_cachorro:.2f} + Serviço(s) extra: R${servico_extra:.2f})')     




