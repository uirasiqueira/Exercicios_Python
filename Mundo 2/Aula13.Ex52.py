'''Faça um programa que leia um número inteiro e diga se ele é
ou não um número primo'''

n = int(input('Digite um numero:'))
s=0
for c in range (1, n+1):
    if n%c==0:
        print('\033[33m', end=' ') #Todo numero que for dividido pela variavel C ou valor de cada loop (e.g 1, 2, 3..) o numero sera colorido!!
        s+=1
    else:
        print('\033[m', end=' ') #Caso nao seja divisivel a cor e torna normal novamente!!
    print(c, end=' ')
if s==2:
    print(f'\n\033[mO numero {n} e primo!')
else:
    print(f'\n\033[mO numero {n} nao e primo!')