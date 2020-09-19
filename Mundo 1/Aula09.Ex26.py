'''Faça um programa que leia uma frase pelo teclado e mostre:

1. Quantas vezes aparece a letra 'A'
2. Em que psição ela aparece pela primeira vez
3. Em que posição ela aparece pela última vez'''

frase = input('Digite uma frase:').upper()
frase1= frase.count('A')
frase2= frase.find('A')
frase3= frase.rfind('A')

print(f' A quantidade de vezes que aparece a letra A na frase e {frase1}')
print(f' A primeira letra A esta localizada no caracter {frase2}')
print(f' A ultima letra A esta localizada no caracter {frase3}')