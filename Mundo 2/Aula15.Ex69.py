'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá
perguntar se o usuário quer ou não continuar. No final mostra:

A) Quantas pessoas tem mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos'''


midade = homens = menoridade = numero = 0
while True:
    print('-'*20)
    idade = int(input('Qual a sua idade: '))
    sexo= ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo [M/F]:')).upper()
    print('-'*20)
    numero += 1
    if idade > 18:
        midade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menoridade += 1
    continuar = str(input('Quer continuar[S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'Foram cadastradas {numero} pessoas. {midade} maiores de 18 anos. {homens} homens e {menoridade} mulheres menores de 20 anos.')