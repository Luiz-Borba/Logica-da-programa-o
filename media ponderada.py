print('insira o valor desejado')
valor1 = float(input())

print('deseja o valor dos meses')
meses = float(input())

meses = (meses*valor1)*0.01
final = meses+valor1
print(f'o seu valor inicial é {valor1} e o valor final é {final}')