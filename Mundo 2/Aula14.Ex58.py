'''Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um numero entre 0 e 10. So que agora o jogador vai
tentar advinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.'''

from random import randint
from time import sleep

print('=' *55)
print('Vou pensar em um numero entre 0 e 10, tente adivinhar...')
print('=' * 55)

#print('PROCESSING...')
#sleep(3)



n = randint(1, 5)
pense = int(input('Qual foi o numero que eu pensei?:'))
print(n)
t=1
while pense !=n:
    n = randint(1, 5)
    pense = int(input(f'\nErrou. Digite novamente um numero: '))
    t+=1
    if pense > 5:
        pense = int(input('Você digitou um numero fora do intervalo. Digite novamente: '))
        t+=1
if pense ==n:
    print(f'Parabens. Mas vocês precisou de {t} palpitespara advinhar o numero que pensei!')


