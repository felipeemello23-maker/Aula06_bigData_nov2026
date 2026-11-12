valor =   float(input('valor da venda: '))

print('''
[1] - Inteira
[2] - Meia entrada (50% de desconto)
[3] - Promoção (30% de Desconto)
''')

desconto = 0
opcao = float(input('informe a opção escolhida: '))
match opcao:
    case 1:
        print('\n sem Desconto')
        
    case 2:
            print('\n Meia (50% de desconto)')
            desconto = valor * 0.50

    case 3:
            print('Promoção (30% de desconto)')
            desconto = valor * 0.30

    case _:
            print('opção Inválida')

if desconto != 0:
      valor_final = valor - desconto
      print(f'Preço: {valor}')
      print(f'desconto: {desconto}')
      print(f'total a pagar: {valor_final}')

else: 
     print('Digite uma das opçêos acima')
