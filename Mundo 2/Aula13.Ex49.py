'''Refaça o desafio 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utiliznado um laço for

print('*.'*20)
print('             Super tabuada')
print('*.'*20)

n = int(input('Digite um numero que gostaria de saber a tabuada:'))
print(f'{n} x 1  = {n*1}')
print(f'{n} x 2  = {n*2}')
print(f'{n} x 3  = {n*3}')
print(f'{n} x 4  = {n*4}')
print(f'{n} x 5  = {n*5}')
print(f'{n} x 6  = {n*6}')
print(f'{n} x 7  = {n*7}')
print(f'{n} x 8  = {n*8}')
print(f'{n} x 9  = {n*9}')
print(f'{n} x 10 = {n*10}')'''

#ou

print('             Super tabuada')
from time import sleep
tabuada = int(input('Qual o numero da tabuada que gostaria de calcular?'))
print('-'*15)
for c in range(0,11):
    print(f'{tabuada} x {c:2} = {c*tabuada}')
    sleep(0.5)
print('-' * 15)