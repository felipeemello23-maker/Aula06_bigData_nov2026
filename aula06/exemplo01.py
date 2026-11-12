
valor =   float(input('valor da venda: '))

print('''
[1] - Pix (12% de Desconto)
[2] - Debito (8% de Desconto)
[3] - Credito (5% de Desconto)
[4] - Dinheiro (15% de Desconto)
''')

operacao = True
Desconto = 0
opcao = int(input('informe a opção escolhida: '))

match opcao:
    case 1:
        print('---Pix---')
        Desconto = valor * 0.12

    case 2:
            print('---Debito---')
            Desconto = valor * 0.08

    case 3:
            print('---Credito---')
            Desconto = valor * 0.05

    case 4:
            print('---Dinheiro---')
            Desconto = valor * 0.15
    case _:
            print('opção Inválida')

#if operacao == True:
if Desconto != 0:
# if opcao in [1, 2, 3, 4]:
       valor_final = valor - Desconto
       print(f'Preço: {valor}')
       print(f'desconto: {Desconto}')
       print(f'total a pagar: {valor_final}')

else: 
     print('Por Favor, escolha uma das opções acima')

