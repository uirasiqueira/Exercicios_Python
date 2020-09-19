''' Desenolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

import math
print('><'*20)
print('       Índice de massa corporea')
print('><'*20)

peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))
imc = peso/(altura**2)

#print('O seu imc e \033[1m{}'.format(round(imc,2)))
#ou
print(f'O seu imc e \033[1;33m{round(imc,2)}\033[m.')

if imc<18.5:
    print('Você esta abaixo do peso!')
elif 18.5<=imc<25:
    print('Você esta no peso ideal!')
elif 25<=imc<30:
    print('Voce esta com sobrepeso!')
elif 30<=imc<=40:
    print('Você esta com obesidade!')
elif imc>40:
    print('Você esta com obesidade morbida, \033[1;31mCUIDADO!!')