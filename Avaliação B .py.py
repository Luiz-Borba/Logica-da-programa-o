print('Digite o valor atual do dolar')
dolar=float(input())
print('digite o tipo de operação ')
print('dolar para real use DR e real para dolar RD')
operação=str(input()).upper()
print('digite o valor que deseja trocar em R$:')
valor=float(input())

if operação=='RD'or operação=='DR':
    if operação =="RD":
        conta=valor/dolar
        print(f'a cotação atual do dólar é:{dolar}')
        print(f'a operação escolhida foi de real para dolar')
        print(f'Portanto, você tem direito a U$: {conta}')
    else:
        conta= valor*dolar
        print(f'a cotação atual do dólar é:{dolar}')
        print(f'a operação escolhida foi de dolar para real')
        print(f'Portanto, você tem direito a R$: {conta}')
else:
    print('valor invalido')
    

