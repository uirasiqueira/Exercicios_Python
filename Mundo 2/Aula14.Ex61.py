'''Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 pirmeiros termos da progressão
usando a estrutura while.'''

a1= int(input('Digite o primeiro termo:'))
r= int(input('Digite a razao da PA:'))
c=0
while c<10:
    print(a1)
    a1 = a1 + r
    c+=1
print('FIM')