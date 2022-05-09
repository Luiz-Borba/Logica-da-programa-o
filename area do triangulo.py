print('Digite o valor do cateto 1')
valor1 = float(input())
print('Digite o valor do cateto 2')
valor2 = float(input())

hipotenusa = (valor1**2) + (valor2**2)
hipotenusa = hipotenusa **0.5
print(f'Portanto, o valor da hipotenusa é: {hipotenusa}')
