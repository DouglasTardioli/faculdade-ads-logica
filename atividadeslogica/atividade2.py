print('\nBem-vindo a sorveteria do Douglas Peixoto Tardioli')


print('-' * 35, 'cardápio', '-' * 35) #Menu que aparece na tela do cliente
print('|', 'N° de bolas', '|', 'Sabor tracional (tr)', '|' , 'Sabor Premium (pr)', '|', 'Sabor Especial (es)', '|')
print('|', '    1      ' , '|', '      R$6,00        ', '|' , '     R$7,00       ',  '|', '      R$8,00       ', '|')
print('|', '    2      ' , '|', '      R$11,00       ', '|' , '     R$13,00      ',  '|', '      R$15,00      ', '|')
print('|', '    3      ' , '|', '      R$15,00       ', '|' , '     R$18,00      ',  '|', '      R$21,00      ', '|')
print('-' * 80)


valor = 0


while True:
  sabor = input('Entre com o valor desejado (tr, pr, es): ')
  if sabor != 'tr' and sabor != 'pr' and sabor != 'es': #se a pessoa escolher algo que não esteja como opção
    print('\n ❌ Escolha incorreta!! tente novamente...')     #mensagem de erro
    continue
  bolas = input('Entre com a quantidade de bolas desejada (1, 2, 3): ')
  if bolas != '1' and bolas != '2' and bolas != '3': #se a pessoa ar algo que não esteja como opção
    print('\n ❌ Escolha incorreta!! tente novamente...')  #mensagem de erro
    continue

 
  if sabor == 'tr': #se o sabor tradiconal for escolhido
    if bolas == '1': #se 1 bola de sorvete for escolhida
      tr_1 = 6
      print(f'Você pediu 1 bola de sorvete no sabor tradiconal: R${tr_1}')
      valor += tr_1
    elif bolas == '2': #se 2 bola de sorvete for escolhida
      tr_2 = 11
      print(f'Você pediu 2 bolas de sorvete no sabor tradiconal: R${tr_2}')
      valor += tr_2
    elif bolas == '3': #se 3 bola de sorvete for escolhida
      tr_3 = 15
      print(f'Você pediu 3 bolas de sorvete no sabor tradiconal: R${tr_3}')
      valor += tr_3
    

  if sabor == 'pr': #se o sabor Premium for escolhido
    if bolas == '1': #se 1 bola de sorvete for escolhida
      pr_1 = 7
      print(f'Você pediu 1 bola de sorvete no sabor Premium: R${pr_1}')
      valor += pr_1
      
    elif bolas == '2': #se 2 bolas de sorvete for escolhida
      pr_2 = 13
      print(f'Você pediu 2 bolas de sorvete no sabor Premium: R${pr_2}')
      valor += pr_2
    elif bolas == '3': #se 3 bolas de sorvete for escolhida
      pr_3 = 18
      print(f'Você pediu 3 bolas de sorvete no sabor Premium: R${pr_3}')
      valor += pr_3

  if sabor == 'es':
    if bolas == '1': #se 1 bola de sorvete for escolhida
      es_1 = 8 
      print(f'Você pediu 1 bola de sorvete no sabor Especial: R${es_1}')
      valor += es_1
    elif bolas == '2': #se 2 bolas de sorvete for escolhida
      es_2 = 15
      print(f'Você pediu 2 bolas de sorvete no sabor Especial: R${es_2}')
      valor += es_2

    elif bolas == '3': #se 3 bolas de sorvete for escolhida
      es_3 = 21
      print(f'Você pediu 3 bolas de sorvete no sabor Especial: R${es_3}')
      valor += es_3
  
  comprar_novamente = input('Dejesa comprar outro sorvete? (s/n)')
  if comprar_novamente == 's' and comprar_novamente == 'S': #se a pessoa escolher compra novamente
      continue                                              #o laço se incia
  elif (comprar_novamente == 'n'):                          #se a pessoa escolher não comprar
    print(f'\nValor da sua compra foi de: R${valor}\n ----------Volte sempre----------') #print do valor final
    break                                                                               #fim da aplicação