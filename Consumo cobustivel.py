print('quantos km voce rodou?')
km = float(input())
print('qual o seu tipo do seu carro escreva apenas A , B ou C')
carro = str(input()).upper()

if carro == 'A':
    carro = 12
    gasto = km/carro
    print(f'seu carro rodou {gasto} por litros de gasolina')
if carro == 'B':
    carro = 9
    gasto = km/carro
    print(f'seu carro rodou {gasto} por litros de gasolina')
if carro == 'c':
    carro = 8
    gasto = km/carro
    print(f'seu carro rodou {gasto} por litros de gasolina')


