'''Escreva um programa para aprovar um empreétimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calucle o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
negado'''

from time import sleep
print('-='*20, 'Bem vindo ao SuperCap, empretimo para o seu Futuro', '-='*20)
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salario? R$'))
anos = float(input('Em quantos anos pretende quitar o emprestimo?'))
prest = casa/(12*anos)


print('AGUARDE UM MOMENTO...')
sleep(3)


if prest <=30/100*sal:
    print('\033[33mParabens, o seu credito de habitação foi aceito\033[m')
    print('A prestação sera de \033[1;31m{:.2f}\033[m reais mensais'.format(prest))
    #print(f'Para quitar a casa no valor de R${casa} em {anos} anos a prestação será de R${round(prest,2)}')
else:
    print('Desculpe, mas o seu emprestimo foi recusado!')


#Voce pode fazer uma simulação aumentando o numero de anos para o salario da pessoa ou vc pode fazer uma outra simulação
# caso a pessoa tivesse um salario maior