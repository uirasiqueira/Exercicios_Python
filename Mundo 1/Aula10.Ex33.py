'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite mais um nummero:'))
n3 = int(input('Digite mais um numero:'))
'''if n1>n2 and n1>n3:
    max= n1
    if n2<n3:
        min = n2
    else:
        min = n3
if n2> n1 and n2>n3:
    max = n2
    if n1<n3:
        min = n1
    else:
        min= n3
if n3>n1 and n3>n2:
    max = n3
    if n1<n2:
        min= n1
    else:
        min= n2

ou'''

min = n1
if n2<n3 and n2<n1:
    min = n2
if n3<n1 and n3<n2:
    min = n3
max = n1
if n2>n1 and n2>n3:
    max=n2
if n3>n1 and n3>n2:
    max=n3
print(f'O valor maximo sera {max} e o valor minimo sera {min}')