print('insira a sua media')
media = float(input())

if media >=6:
    print('aprovado')
else:
    if media<4:
        print('reprovado')
    else:
        if media >=4 and media<6:
            print('exame final')