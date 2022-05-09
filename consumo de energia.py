print('ola usuario digite o tipo da sua residencia')
print('R para residencioal, I para industria e C para comercio')
tipo = str(input())
print('digite o Kw/H')
energia = float(input())

if energia<0:
    print('valor invalido')
    exit()
else:
    if (energia >=0 and energia <=500) and (tipo=='r' or tipo=='R'):
       preco=0.40
       imposto=0.1
       gasto=energia*preco
       taixa=gasto*imposto
       gastoTotal=gasto+taixa
       print(f'a tarifa para o seu gasto sem imposto é de : R${gasto} , o imposto é de: R${taixa}0 e o seu gasto total é de: R${gastoTotal}')

    if (energia >=0 and energia >500) and (tipo=='r' or tipo=='R'):
       preco=0.65
       imposto=0.12
       gasto=energia*preco
       taixa=gasto*imposto
       gastoTotal=gasto+taixa
       print(f'a tarifa para o seu gasto sem imposto é de : R${gasto} , o imposto é de: R${taixa}0 e o seu gasto total é de: R${gastoTotal}')

    if (energia >=0 and energia <=1000) and (tipo=='c' or tipo=='C'):
       preco=0.55
       imposto=0.15
       gasto=energia*preco
       taixa=gasto*imposto
       gastoTotal=gasto+taixa
       print(f'a tarifa para o seu gasto sem imposto é de : R${gasto} , o imposto é de: R${taixa}0 e o seu gasto total é de: R${gastoTotal}')

    if (energia >=0 and energia >1000) and (tipo=='c' or tipo=='C'):
       preco=0.60
       imposto=0.16
       gasto=energia*preco
       taixa=gasto*imposto
       gastoTotal=gasto+taixa
       print(f'a tarifa para o seu gasto sem imposto é de : R${gasto} , o imposto é de: R${taixa}0 e o seu gasto total é de: R${gastoTotal}')

    if (energia <=5000 ) and (tipo=='i' or tipo=='I'):
       preco=0.55
       imposto=0.20
       gasto=energia*preco
       taixa=gasto*imposto
       gastoTotal=gasto+taixa
       print(f'a tarifa para o seu gasto sem imposto é de : R${gasto} , o imposto é de: R${taixa}0 e o seu gasto total é de: R${gastoTotal}')

    if (energia >5000) and (tipo=='c' or tipo=='C'):
       preco=0.60
       imposto=0.22
       gasto=energia*preco
       taixa=gasto*imposto
       gastoTotal=gasto+taixa
       print(f'a tarifa para o seu gasto sem imposto é de : R${gasto} , o imposto é de: R${taixa}0 e o seu gasto total é de: R${gastoTotal}')



    