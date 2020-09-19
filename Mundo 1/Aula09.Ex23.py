'''Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos digitos separados'''

numero = input('Digite um numero:')
print('Unidade:', numero[3:])
print('Dezena:', numero[2:])
print('Centena:', numero[1:])
print('Milhar:', numero[0:])

#ou

#print('Unidade:',numero[3])
#print('Dezena:', numero[2])
#print('Centena:', numero[1])
#print('Milhar:', numero[0])