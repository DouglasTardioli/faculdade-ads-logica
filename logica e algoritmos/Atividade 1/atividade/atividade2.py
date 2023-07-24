print('Bem-vindo a sorveteria do Douglas Peixoto Tardioli')

print('-' * 35, 'cardápio', '-' * 35)
print('|', 'N° de bolas', '|', 'Sabor tracional (tr)', '|' , 'Sabor Premium (pr)', '|', 'Sabor Especial (es)', '|')
print('|', '    1      ' , '|', '      R$6,00        ', '|' , '     R$7,00       ',  '|', '      R$8,00       ', '|')
print('|', '    2      ' , '|', '      R$10,00       ', '|' , '     R$12,00      ',  '|', '      R$14,00      ', '|')
print('|', '    3      ' , '|', '      R$14,00       ', '|' , '     R$17,00      ',  '|', '      R$20,00      ', '|')
print('-' * 80)

tr_1 = 6

while True:
  
  sabor = input('Entre com o valor desejado (tr, pr, es): ')
  bolas = input('Entre com a quantidade de bolas desejada (1, 2, 3): ')
  
  if sabor == 'tr':
    if bolas == '1':
      valor = 0
      print(f'Você pediu 1 bola de sorvete no sabor tradiconal: R${tr_1}')
      
      comprar_novamente = input('Dejesa comprar outro sorvete? (s/n)')
      if comprar_novamente == 's':
          valor += tr_1
          print(valor)
          continue
      else:
        break
    elif bolas == '2':
      valor = 7
      print(f'Você pediu 2 bolas de sorvete no sabor tradiconal: R${valor}')

    elif bolas == '3':
      valor = 8
      print(f'Você pediu 3 bolas de sorvete no sabor tradiconal: R${valor}')
    

  if sabor == 'pr':
    if bolas == '1':
      valor = 10
      print(f'Você pediu 1 bola de sorvete no sabor Premium: R${valor}')
    elif bolas == '2':
      valor = 12
      print(f'Você pediu 2 bolas de sorvete no sabor Premium: R${valor}')
    elif bolas == '3':
      valor = 14
      print(f'Você pediu 3 bolas de sorvete no sabor Premium: R${valor}')

  if sabor == 'es':
    if bolas == '1':
      valor = 14
      print(f'Você pediu 1 bola de sorvete no sabor Especial: R${valor}')
    elif bolas == '2':
      valor = 17
      print(f'Você pediu 2 bolas de sorvete no sabor Especial: R${valor}')
    elif bolas == '3':
      valor = 20
      print(f'Você pediu 3 bolas de sorvete no sabor Especial: R${valor}')
