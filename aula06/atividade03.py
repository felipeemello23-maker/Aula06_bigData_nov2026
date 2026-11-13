for i in range(5):
    print( )
    valor = float(input('informe o valor '))

if valor >= 200:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f'valor do  desconto {desconto}\n Valor Final  para  pagar {valor_final}')

else: 
    print(f'Valor não recebe desconto, valor a ser pago {valor}')