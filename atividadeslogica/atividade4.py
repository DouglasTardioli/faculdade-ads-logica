print('\nBem-vindo ao Controle de Colaboradores do Douglas Peixoto Tardioli')

lista_colaborador = []
id_colaborador = 0

def cadastrar_colaborador(id): #Função de cadastrar colaborador(a)
  print('cadastrar Colaborador: ')
  nome = input('Qual o nome do(a) colaborador(a): ')
  setor = input('Qual o setor de trabalho: ')
  salario = float(input('Quanto essa pessoa irá receber: R$'))
  
  dicionario_colaborador = {
    'id' : id_colaborador,
    'nome' : nome,
    'setor' : setor,
    'salario' : salario,
  }

  lista_colaborador.append(dicionario_colaborador.copy()) #copia do dicionario para a lista global

def consultar_colaborador(): #Função de consulta colaborador(a)
  print('Consultar Colaborador: ')
  while True: #loop de menu para consulta colaborador(a)
    consultar_colaborador = input('\nEntre com a opcão desejada: \n' + #Menu de escolha do tipo de consulta
                                    '1 - Consultar todos\n' +
                                    '2 - Consultar por Id\n' +
                                    '3 - Consultar por setor\n' +
                                    '4 - Retornar ao menu principal\n' +
                                    '|-> ')
    if consultar_colaborador == '1': #Se Consultar por Todos os colaboradores for escolhida
      print('Você escolheu consultar todos: ')
      for colaborador in lista_colaborador:
        print('-' * 35)
        for key, value in colaborador.items():
          print(f'{key} : {value}')
        print('-' * 35)
    elif consultar_colaborador == '2': #Se Consultar por ID dos colaboradores for escolhida
      print('Você escolheu consultar por Id: ')
      id_desejado = int(input('Entre com o ID do colaborador: '))
      for colaborador in lista_colaborador:
          if colaborador['id'] == id_desejado:
             print('-' * 35)
             for key, value in colaborador.items():
                print(f'{key} : {value}')
             print('-' * 35)
    elif consultar_colaborador == '3': #Se Consultar por Setor dos colaboradores for escolhida
      print('Você escolheu consultar por Setor: ')
      setor_desejado = input('Entre com o Setor do colaborador: ')
      for setor in lista_colaborador:
          if setor['setor'] == setor_desejado:
             print('-' * 35)
             for key, value in setor.items():
                print(f'{key} : {value}')
             print('-' * 35)
    elif consultar_colaborador == '4': #Se voltar para o menu Principal for escolhida
      return
    else: #erro para retornar ao começo deste loop
      print('\n ❌ Opção invalida! tente novamente')
      continue

def remover_colaborador(): #Função para remover coladorador (a)
  print('Você escolheu remover colaborador: ')
  id_desejado = int(input('Entre com o ID do colaborador que deseja remover: '))
  for colaborador in lista_colaborador:
      if colaborador['id'] == id_desejado:
        lista_colaborador.remove(colaborador)
        print('\nColaborador Removido! ✔') 

#Inicia o programa principal apartir daqui --------- */

while True: #loop do menu principal
  print('\nPrograma para Cadastrar, consultar ou remover colaborador')
  menu = input('\nEntre com a opcão desejada: \n' + #Menu de entrada das opções
                '1 - Cadastrar colaborador\n' +
                '2 - Consultar Colaborador\n' +
                '     1 - Consultar todos\n' +
                '     2 - Consultar por Id\n' +
                '     3 - Consultar por setor\n' +
                '     4 - Retornar ao menu\n' + 
                '3 - Remover colaborador\n' +
                '4 - Encerrar programa\n' +
                '|-> ' )
  
  if menu == '1': #Cadastrar colaborador 
    id_colaborador = id_colaborador + 1 #somar Id
    cadastrar_colaborador(id_colaborador)
  elif menu == '2': #entra no menu consultar colaborador(a)
    consultar_colaborador()
  elif menu == '3':
    remover_colaborador()
  elif menu == '4':
    print('\n----------->Encerrando programa<----------------')
    break
  else:
    print('\n ❌ Opção invalida! tente novamente')
    continue