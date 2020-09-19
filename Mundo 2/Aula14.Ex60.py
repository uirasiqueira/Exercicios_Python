'''Faça um programa que leia um numero qualquer e mostre o seu fatorial.
Ex. 5! = 5x4x3x2x1 = 120.'''

n=int(input('Digite um numero e descubra o seu fatorial: '))
y=n
while y !=1:
   n = n*(y-1)
   y=y-1
print(f'O valor fatorial e de {n}')

'''n = int(input('Digite um numero e descubra o seu fatorial: '))
y = n
for c in range(1, n):
    n = n * (y - 1)
    y = y - 1
print(f'O valor fatorial e de {n}')'''
