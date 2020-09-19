'''Crie um programa que leia o ano de nascimento de sete pessoas. No final
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date
m=0
x=0
a=date.today().year
for c in range (1,8):
    idade = int(input('\033[33mDigite o seu ano de nascimento:'))
    if a - idade < 21:
        m += 1
    elif a - idade >=21:
        x+=1
print(f'{m} pessoas ainda não atingiram a maioridade e {x} pessoas ja são maiores de idade!')