'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando a flag)'''

print('~' * 30)
print('Super contador')
print('~' * 30)


n = c = s = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    c += 1
    s += n
t = s-999
c = c-1
print(f'Foram digitados {c} e a soma dos valores foram {t} ')
