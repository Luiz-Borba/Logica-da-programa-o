print('insira o primeiro valor')
numero1=(float(input()))

print('insira o primeiro valor')
numero2=(float(input()))

print('insira o primeiro valor')
numero3=(float(input()))

if numero1>numero2:
    if numero1>numero3:
        print(f'o maior numero é :{numero1}')
        
if numero2>numero3:
    if numero2>numero1:
        print(f'o maior numero é :{numero2}')
if numero3>numero2:
    if numero3>numero1:
        print(f'o maior numero é :{numero3}')

if numero1<numero2:
    if numero1<numero3:
        print(f'o menor numero é :{numero1}')
        
if numero2<numero3:
    if numero2<numero1:
        print(f'o menor numero é :{numero2}')
if numero3<numero2:
    if numero3<numero1:
        print(f'o menor numero é :{numero3}')
if numero1==numero2==numero3:
    print('os numeros são iguais')
else:
    if numero1 == numero2:
        print('os numeros são iguais')
    if numero2 == numero3:
        print('os numeros são iguais')
    if numero3 == numero1:
        print('os numeros são iguais')