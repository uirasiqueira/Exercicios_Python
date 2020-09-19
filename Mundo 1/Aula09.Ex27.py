'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente'''

nome = input('Digite o seu nome:').upper().split()

nome1 = nome[0]
nome2 = nome[-1]
print(f'Primeiro nome: {nome1}\nUltimo nome: {nome2}')
