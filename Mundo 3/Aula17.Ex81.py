'''Crie um programa que vai ler vários números e vai colocar em uma [].
Depois disso, mostre:

A) Quantos números foram digitados;
B) A lista de valores, ordenados de forma decrescente;
C) Se o valor 5 foi ou não digitado e está ou não na lista.'''


valores= []
continuar = ''
cont = 0
while True:
    numero = int(input('Digite um número: '))
    cont+=1
    valores.append(numero)
    continuar = str(input('Quer continuar [S/N]:')).upper()
    if continuar == 'N':
        break
print('-.'*20)
print(f'Foram digitados {cont} valores')
print('-.'*20)
valores.sort(reverse=True)
print(f'O valores digitados foram: ', end='')
print(valores)
print('-.'*20)
if 5 in valores:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
print('-.'*20)