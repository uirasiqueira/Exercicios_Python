'''Desenolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão'''

print('='*30)
print('    Progressão aritimetica')
print('='*30)

a1= int(input('Digite o primeiro termo:'))
r= int(input('Digite a razao da PA:'))
an= a1+(10-1)*r
for c in range(a1, an+r, r):
    print(c,'->', end=' ')
print('FIM')


