'''Desenvolva um programa que leia 6 números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o'''

a = 0
e = 0
for c in range (1,7):
    p = int(input(f'Digite o {c}° valor:'))
    if p%2==0:
        a+=p
        e+=1

print(f'A soma dos {e} numeros pares foi {a}!')