print('digite o valor do produto')
produto = float(input())

if produto>=20:
    porcentagem =produto *0.45
    produto=produto+porcentagem
    print(f'o valor de venda do produto é {produto}')
else:
    porcentagem =produto *0.3
    produto= produto+porcentagem 
    print(f'o valor de venda do produto é {produto}')

