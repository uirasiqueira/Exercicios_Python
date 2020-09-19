'''Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa

    Seu programa devera realizar a operação solicitada em cada caso'''

v1= int(input('Digite um numero: '))
v2 = int(input('Digite outro numero: '))
operacao = 0
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')
operacao = int(input('Para realizar uma das operações anteriores, escolha uma das opções numericas: '))

while operacao!=0:
    if operacao == 1:
        v = v1+v2
        operacao = int(input(f'O valor sera {v}. Qual a proxima operação a ser realizada? '))
    if operacao == 2:
        v = v1*v2
        operacao = int(input(f'O valor sera {v}. Qual a proxima operação a ser realizada? '))
    if operacao == 3:
        if v1>v2:
            operacao = int(input(f'O maior valor sera {v1}. Qual a proxima operação a ser realizada? '))
        else:
            operacao = int(input(f'O maior valor sera {v2}. Qual a proxima operação a ser realizada? '))
    if operacao == 4:
        v1 = int(input('Digite um novo numero: '))
        v2 = int(input('Digite mais um novo numero: '))
        operacao = int(input('Qual a proxima operação a ser realizada? '))
    if operacao == 5:
        operacao = 0
print('Fim')

