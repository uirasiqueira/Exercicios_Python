'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando usuário
digitar o valor 999, que é a codição de parada. No final, mostre quantos números foram digitados e mostre a soma
entre eles (desconsiderando a flag)'''

valores = soma = 0
while True:
    n = int(input('Digite um número: [Para parar digite 999]'))
    if n == 999:
        break
    valores += 1
    soma += n

print(f' Foram digitados {valores} números e a soma foi {soma}')
