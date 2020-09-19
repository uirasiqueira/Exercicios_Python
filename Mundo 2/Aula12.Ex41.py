''' A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre a sua categoria, de acordo com a idade:

- Até  anos: mirim
- Até 15 anos: infantil
- Até 19 anos: junior
- Até 20 anos: Sênior
- Acima: Master'''

print('~.'*20)
print(' '*3, 'Confederação nacional de natação')
print('~.'*20)
from datetime import date
nasc = int(input('Qual o ano de nascimento do atleta?'))
idade = date.today().year - nasc

if idade <=9:
    print('\033[33mCategoria Mirim')
elif idade <=14:
    print('\033[33mCategoria Infantil')
elif idade <=19:
    print('\033[33mCategoria Junior')
elif idade ==20:
    print('\033[33mCategoria Sênio')
elif idade>20:
    print('\033[33mCategoria Master')


