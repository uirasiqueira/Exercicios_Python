'''Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador

O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep
n= randint(0,5)
print('=' *55)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('=' * 55)
pense = int(input('Qual foi o numero que eu pensei?:'))
print('PROCESSING...')
sleep(3)
if pense == n:
    print('Parabens, você conseguiu me vencer!')
else:
    print(f'GANHEI, o numero que eu pensei foi {n} e não {pense}!')
