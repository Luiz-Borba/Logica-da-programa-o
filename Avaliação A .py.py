print('Digite o preço de custo do produto')
preço=float(input())
print('Digite a % de comissão do vendedor')
vendedor=float(input())
print('Digite a % de desconto do cliente:')
desconto=float(input())

vendedor=(vendedor/100*preço)+preço
comissão=vendedor-preço
produto=preço-vendedor
comissãov=vendedor-produto
valordesconto=(desconto/100)*vendedor
valorF=preço+comissão-valordesconto
print(f'Preço do produto com comissão do vendedor:{vendedor}')
print(f'Valor da comissão do vendedor:{comissão}')
print(f"Valor do desconto do cliente:{valordesconto}")
print(f'valor final é de :{valorF}')
