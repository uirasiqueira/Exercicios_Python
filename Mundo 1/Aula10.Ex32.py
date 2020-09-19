'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

from datetime import date
import random
#ano = random.randint(1990, 2020)
ano= int(input('Qual o ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano ==0:
    ano = date.today().year
if ano%4 != 0:
    if ano%400 !=0:
        print (f'O ano de {ano} não e bisexto')
    else:
        print(f'O ano de {ano} e bissexto')
else:
        if ano%100 !=0:
            print(f'O ano de {ano} sera bissexto')
        else:
            print(f'O ano de {ano} não sera bissexto')