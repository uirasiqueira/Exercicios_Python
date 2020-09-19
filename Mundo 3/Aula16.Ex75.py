'''Desenvolva um pograma que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
mostre:
A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado primeiro valor 3;
C) Quais foram os números pares.'''


'''tupla = ((int(input('Digite um valor: '))), (int(input('Digite um valor: '))),
         (int(input('Digite um valor: '))), (int(input('Digite um valor: '))))
print(f'Você digitou os valores {tupla}')
if 9 not in tupla:
    print(f'O número 9 não foi digitado')
else:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 not in tupla:
    print('O número 3 não foi digitado')
else:
    print(f'O número 3 apareceu na {tupla.index(3)+1}ª posição')
print(f'Os números pares digitados foram: ', end='')
for c in tupla:
    if c%2==0:
        print(f'|{c}|', end='')'''

#ouGuanabara method

tupla = ((int(input('Digite um valor: '))), (int(input('Digite um valor: '))),
         (int(input('Digite um valor: '))), (int(input('Digite um valor: '))))

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for n in tupla:
    if n %2==0:
        print(f'{n} ', end='')
