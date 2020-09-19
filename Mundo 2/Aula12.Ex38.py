''' EScreva um programa que leia dois nuúmero inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro número é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

print('=+'*20)
print(' '*10, 'Data processing')
print('=+'*20)
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero'))

if n1>n2:
    print(f'O numero {n1} e maior que o {n2}!')
elif n1<n2:
    print(f'O numero {n2} e maior que o {n1}!')
elif n1==n2:
    print('Não existe valor maior, os dois são iguais!')