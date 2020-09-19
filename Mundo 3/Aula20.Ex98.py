'''Faça um programa que tenha uma função chamada contador(), que receba
três parâmetos: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada'''

from time import sleep
'''def contador(a,b,c):
    print('-'*30)
    print(f'Contagem de {a} até {b-1} de {c} em {c}')
    for c in range (a,b,c):
        print(f'{c} ', end='')
        sleep(0.5)
    print()
    print('FIM!')


contador(1,11,1)
contador(10,1,-2)
contador(int(input(f'Início:')))
#Para na contagem personalizada'''

#Guanabara method

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i<f:
        cont=i
        while cont<=f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont+=p
        print('FIM!')
    else:
        cont=i
        while cont>=f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont-=p
        print('FIM!')


#programa principal
contador(1,10,1)
contador(10,0,2)
print('-'*20)
print('Agora é a sua vez de personalizar a contagem!')
ini=int(input('Início: '))
fim = int(input('Fim:  '))
pas= int(input('Passo: '))
contador(ini, fim, pas)
