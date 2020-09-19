''' Crie um programaue leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR'''
n = int(input('Digite um numero:'))
resto = n%2
if resto == 0:
    print(f'O numero {n} e um numero par!')
else:
    print('O numero e impar!')