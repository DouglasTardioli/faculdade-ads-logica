print('\nBem-vindo ao banho e tosa do Douglas Peixoto Tardioli\n')

preco = 0
multiplicador = 0

def pesoCachorro(): #Função de Peso do Cachorro
  while True:
          try:
            peso = int(input('Qual o peso do cachorro (kg) 🐶: ')) #Entrar com o peso do cachorro
            if peso < 3: 
                preco = 40
                return preco
            elif peso >= 3 and peso < 10:
                preco = 50
                return preco
            elif peso >= 10 and peso < 30:
                preco = 60
                return preco
            if peso >= 30 and peso < 50:
                preco = 70
                return preco
            else:
                print('\n ❌ Não aceitamos cachorros tão grandes. \n' + #erro de peso muito alto
                    'Por favor, entre com o peso do cachorro novamente\n')
          except ValueError:
              print('\n ❌ Você digitou um valor não numerico \n' + #erro valor não numerico 
                    'Por favor, entre com o peso do cachorro novamente\n')
            

def peloCachorro(): #Função para escolha de Peso do cachorro
  while True:
      pelo_cachorro = input('Qual o Pelo do cachorro \n' + #menu para escolha do pelo
                            'c - Pelo Curto\n' +
                            'm = Pelo Médio\n' +
                            'l = Pelo Longo\n' +
                            '🐶 ')
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
          print(' ❌ Digite uma das opções acima.')



def servicoExtra(): #Função para escolher se deseja algum serviço extra
    accum = 0
    while True: #Loop menu de escolhas extras
      extra = input('Deseja adicionar mais algum serviço: \n' + #menu para a escolha de serviços extras
                            '0 - Não, desejo finalizar.\n' +
                            '1 - Cortes de unhas - R$10,00\n' +
                            '2 - Escovar Dentes - R$12,00\n' +
                            '3 - Limpeza de orelhas - R$15,00\n' +
                            '🐶 ')
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
          print('\n ❌ Digite uma das opções acima.')

#variáveis de armazenamento
peso_cachorro =  pesoCachorro()
print('-' * 50) #espaço entre perguntas    
pelo_cachorro =  peloCachorro()
print('-' * 50) #espaço entre perguntas    
servico_extra = servicoExtra()
print('-' * 50) #espaço entre perguntas 



total = (peso_cachorro * pelo_cachorro) + servico_extra #total que a pessoa deverá pagar
#print resultado com total e calculos para o total
print(f'Total a pagar: R${total:.2f}\n' + 
      f'(peso: R${peso_cachorro:.2f} * pelo: R${pelo_cachorro:.2f} + Serviço(s) extra: R${servico_extra:.2f})')