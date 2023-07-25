lista_colaborador = []
id_colaborador = 0

def cadastrar_colaborador(id):
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

  lista_colaborador.append(dicionario_colaborador.copy())
def consultar_colaborador():
  print('Consultar Colaborador: ')
  while True:
    consultar_colaborador = input('\nEntre com a opcão desejada: \n' +
                                    '1 - Consultar todos\n' +
                                    '2 - Consultar por Id\n' +
                                    '3 - Consultar por setor\n' +
                                    '4 - Retornar ao menu principal\n' +
                                    '-> ')
    if consultar_colaborador == '1':
      print('Você escolheu consultar todos: ')
      for colaborador in lista_colaborador:
        print('-' * 20)
        for key, value in colaborador.items():
          print(f'{key} : {value}')
        print('-' * 20)
    elif consultar_colaborador == '2':
      print('Você escolheu consultar por Id: ')
      id_desejado = int(input('Entre com o ID do colaborador: '))
      for colaborador in lista_colaborador:
          if colaborador['id'] == id_desejado:
             print('-' * 20)
             for key, value in colaborador.items():
                print(f'{key} : {value}')
             print('-' * 20)

    elif consultar_colaborador == '3':
      print('Você escolheu consultar por Setor: ')
      setor_desejado = input('Entre com o Setor do colaborador: ')
      for setor in lista_colaborador:
          if setor['setor'] == setor_desejado:
             print('-' * 20)
             for key, value in setor.items():
                print(f'{key} : {value}')
             print('-' * 20)
    elif consultar_colaborador == '4':
      return
    else:
      print('Opção invalida! tente novamente')
      continue

def remover_colaborador():
  print('Você escolheu remover colaborador: ')
  id_desejado = int(input('Entre com o ID do colaborador que deseja remover: '))
  for colaborador in lista_colaborador:
      if colaborador['id'] == id_desejado:
        lista_colaborador.remove(colaborador)
        print('Colaborador Removido!')


# --------------------- MAIN ------------
while True:
  print('\nBem-vindo ao ______ Douglas Peixoto Tardioli')
  print('\nPrograma para Cadastrar, consultar ou remover colaborador')
  menu = input('\nEntre com a opcão desejada: \n' +
                '1 - Cadastrar colaborador\n' +
                '2 - Consultar Colaborador\n' +
                '     1 - Consultar todos\n' +
                '     2 - Consultar por Id\n' +
                '     3 - Consultar por setor\n' +
                '     4 - Retornar ao menu\n' +
                '3 - Remover colaborador\n' +
                '4 - Encerrar programa\n' +
                '-> ' )
  
  if menu == '1':
    id_colaborador = id_colaborador + 1
    cadastrar_colaborador(id_colaborador)
  elif menu == '2':
    consultar_colaborador()
  elif menu == '3':
    remover_colaborador()
  elif menu == '4':
    print('Encerrando programa.')
    break
  else:
    print('Opção invalida! tente novamente')
    continue
