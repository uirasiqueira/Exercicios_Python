'''Escreve um programa que escreva um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de Fibonacci.

Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

 Sequencia de Fibonacci é a soma de dois números inteiros , cada termo subsequente corresponde a soma dos dois anteriores'''
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1= 0
t2= 1
print('~'* 30)
print(f'{t1} -> {t2}', end= '')
cont = 3
while cont<=n:
    t3= t1+t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont+=1

print('-> fim')