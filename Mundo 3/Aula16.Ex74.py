'''Crie um programa que vai gerar cinco número aleatórios e colocar
em cada uma tupla.
Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla'''

from random import randint

'''t = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

for c in range(0, len(t)):
    print('->',t[c], end='')
    if c == 0:
        menor = t[c]
        maior = t[c]
    else:
        if t[c] > maior:
            maior = t[c]
        if t[c] < menor:
            menor = t[c]
print(f'\nO número maior é {maior}\nO número menor é {menor}')'''


#Guanabara method

t = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Os valores sorteados foram: ', end='')
for n in t:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(t)}')
print(f'O menor valor sorteado foi {min(t)}')