'''Faça um programa que ajude um jogador da megasena a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
#Guanabara method
from time import sleep
from random import randint

print('.~'*30)
print('{:^60}'.format('Jogo da Mega Sython'))
print('.~'*30)

'''lista =[]
for c in range(0,6):
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
lista.sort()
print(f'Os números sorteados foram {lista}')'''

jogos=[]#lista maior
quant= int(input('Quantos jogos você quer que eu sorteie?'))
lista = []#lista menor

tot=1
while tot<=quant:#Número de jogos
    cont = 0# Valor para indicar o número de resultados por jogos
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)



