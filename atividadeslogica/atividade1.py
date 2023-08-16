print('\nBem-vindo a loja do Douglas Peixoto Tardioli')
print('\nCalcular seu desconto: ')

#Valor de uma Unidade
valor_unitario = float(input('\nQual o valor do produto: R$'))
#quantidade do Produto
qtd_produto = int(input('Qual a quantidade do produto: '))

#valor final = valor da unidade * a quantidade de produtos
valor_final_produto = valor_unitario * qtd_produto
#print do valor sem desconto
print('o valor SEM desconto é de R${:.2f}'.format(valor_final_produto))

#até 200 produtos o valor final não receberá desconto
if qtd_produto < 200:
    valor_final_produto
    print('desconto somente acima de 200 produtos')

#acima de 200 até 1000, desconto será de 5%
elif qtd_produto >= 200 and qtd_produto < 1000:
    desconto_05 = valor_final_produto - (valor_final_produto * 0.05)
    print('o valor COM desconto é de R${:.2f} (desconto de 5%)'.format(desconto_05))

#acima de 1000 até 2000, desconto será de 10%
elif qtd_produto >= 1000 and qtd_produto < 2000:
    desconto_10 = valor_final_produto - (valor_final_produto * 0.10)
    print('o valor COM desconto é de R${:.2f} (desconto de 10%)'.format(desconto_10))

#acima de 2000, desconto será de 15%
else:
    desconto_15 = valor_final_produto - (valor_final_produto * 0.15)
    print('o valor COM desconto é de R${:.2f} (desconto de 15%)'.format(desconto_15))