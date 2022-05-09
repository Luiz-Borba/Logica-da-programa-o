valor1 = float(input("Digite o valor 1 de peso 1: "))
peso1 = float(input("Digite o peso 1: "))
valor2 = float(input("Digite o valor 1 de peso 2: "))
peso2 = float(input("Digite o peso 2: "))
valor3 = float(input("Digite o valor 1 de peso 3: "))
peso3 = float(input("Digite o peso 3: "))
valor4 = float(input("Digite o valor 1 de peso 4: "))
peso4 = float(input("Digite o peso 4: "))

media1 = valor1 * peso1
media2 = valor2 * peso2
media3 = valor3 * peso3
media4 = valor4 * peso4

media = media1 + media2 + media3 + media4
pesos = peso1 + peso2 + peso3 + peso4

mediaPonderada= media / pesos

print("Sua média ponderada é: " + str(mediaPonderada))
#po professor esse exercicio me deixou com dor de cabeça em