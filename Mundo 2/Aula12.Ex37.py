'''Escreva um programa que leia um número interio qualquer e peça ao usuário escolher qual
será a base de conversão

1- para binário
2- para octal
3- hexadecimal'''

print('============== Sistema de conversão numerica ==============')
num = int(input('Escolha um numero:'))
print ('''O sistema disponibiliza 3 bases numericas.
Digite 1 >> Binario <<
Digite 2 >> Octal <<
Digite 3 >> Hexadecimal << ''')

opçao = int(input('Digite a sua opção:'))
if opçao == 1:
    print (f'O valor de {num} em Binario sera:', bin(num)[2:])
elif opçao == 2:
    print (f'O valor de {num} em Ocatal sera:', oct(num)[2:])
elif opçao == 3:
    print (f'O valor de {num} em Hexadecimal sera:', hex(num)[2:])
else:
   print('Digite uma base de comversao \033[33mvalida!!')

