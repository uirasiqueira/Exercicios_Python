''' Desenovla um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R# 0,50
por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas'''

print('=-=-=-=-=-=-=-Bem vindo a FlixNet, uma viagem para o mundo magico de BOB =-=-=-=-=-=-=')

d = float(input('Qual a distância que você ira percorrer na sua viagem?:'))
'''if d <= 200:
    preço = d*0.5
    print(f'O valor da passagem sera de {preço} euros')
else:
    preço = d*0.45
    print(f'O valor da passagem sera de {preço} euros')''' #<<< entre aspas temos o comentario

preço = d*0.5 if d<=200 else d*0.45
print(f'O preço da sua viagem sera de {preço}')