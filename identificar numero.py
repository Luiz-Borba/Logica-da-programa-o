print('se voce escolher a primeira palvra tem que escolher todas vezes a primeira palvra e assim sucessivamente')

print('mesa ,carro ,boneca e machado')
palavra1 = str(input()).upper().strip()[0]

print('comendo , andando,brincando e arvore')
palavra2 = str(input()).upper().strip()[0]

print('jantar , passeio , amigos e parque')
palavra3 = str(input()).upper().strip()[0]

print('dormir,sorvete , sujou e felicidade')
palavra4 = str(input()).upper().strip()[0]

'''mesa comendo jantar dormir'''
'''carro andadno passeio e sorvete'''
'''boneca brincando amigos e sujou'''
'''machado arvore parque e felicidade'''

if palavra1 =='M'and palavra2=='C' and palavra3 =='J'and palavra4 =='D':
    print ('As crianças estavão comendo na mesa de jantar e logo apos a refeição foram dormir')

if palavra1 =='C'and palavra2=='A' and palavra3 =='P'and palavra4 =='S':
    print('fomos passear de carro e no meio do passeio tomamas um sorvete')

if palavra1 =='B'and palavra2=='B' and palavra3 =='A'and palavra4 =='S':
    print('as criasnças estavão brincando com bonecas e seus amigos a sujarão')

if palavra1 =='M'and palavra2=='A' and palavra3 =='P'and palavra4 =='F':
    print('o homem estava com toda a sua felicidade quando cortou aquela arvore no parque com seu machado')