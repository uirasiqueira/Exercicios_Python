'''Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifício, indo de 10 até 0, com uma pause de 1
segundo entre eles'''

import emoji
from time import sleep
for c in range(10,0,-1):
    print(c)
    sleep(1)
print((emoji.emojize(':fireworks:', use_aliases=True)*10), '\033[32mWelcome to newyear\033[m', emoji.emojize(':fireworks:', use_aliases=True)*10)
