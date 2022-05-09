print('insira seu primeiro numero')
numero1 = float(input())
print('insira seu segundo numero')
numero2 = float(input())

if numero1==numero2:
        print('os numeros são iguais')
else:
    if numero1 > numero2:
        print(f'o seu numero maior é :{numero1}')
    else:
        print(f'o seu numero maior é : {numero2}')
