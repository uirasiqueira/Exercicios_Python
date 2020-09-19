'''Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando
os espaços'''

frase= str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ' '.join(palavra)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso+=junto[letra]
if inverso==junto:
    print('Temos um palindromo')
else:
    print('Nao temos um palindromo')

print(inverso)

#frase = str(input('Escreva uma frase:')).upper()
#inverso= frase[::-1]
#print(f'A frase {frase} escrita de tras para frente e {inverso}')
#if frase==inverso:
#    print('E um palindromo')
#else:
#    print('Nao e um palindromo')

#ou

#frase = str(input('Escreva uma frase:'))
#if frase==frase[::-1]:
#    print('E um palindromo')
#else:
#    print('Nao e um palindromo')
