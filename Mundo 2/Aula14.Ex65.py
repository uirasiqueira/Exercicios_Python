'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução
mostre as médias entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores'''

sv = media = contador = maior = menor = 0
v = 'S'
while v!='N':
    contador += 1
    n = int(input('Digite um número inteiro:'))
    v = str(input('Quer continuar? [S/N]: ')).upper()
    sv += n
    media = sv/contador
    if contador == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'A média dos valores é {media}, o valor maior foi {maior} e o menor valor foi {menor}')