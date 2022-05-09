print('digite sua nota')
numero = int(input())
if numero>=0 and numero<=49:
    print('insuficiente')
if  numero>=50 and numero<=64:
    print('regular')
if numero>=65 and numero<=84:
    print('bom')
if numero>=85 and numero<=100:
    print('otimo')
if numero >100 or numero<0:
    print('nota invalida')
    
