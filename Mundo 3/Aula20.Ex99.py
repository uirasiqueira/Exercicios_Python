'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.
Seu programa tem que analisar e dizer qual deles é o maior.'''
#Não fiz!

from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-'*30)
    print('\nAnalisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3),
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} valores ao todos.')
    print(f'O maior valor informado foi {maior}.')


#programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1, 2)
maior(6)
maior()